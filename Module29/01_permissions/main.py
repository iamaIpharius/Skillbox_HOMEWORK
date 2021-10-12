from collections.abc import Callable
import functools


def check_permission(role: str):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if role in user_permissions:
                    return func(*args, **kwargs)
                raise PermissionError
            except PermissionError as ex:
                print(f'{ex} У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapper

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
