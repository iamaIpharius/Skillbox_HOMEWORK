from collections.abc import Callable
import functools


def decorator_with_args_for_any_decorator(decorator):
    def decorator_maker(*args, **kwargs):
        @functools.wraps(decorator)
        def wrap(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)

        return wrap

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrap(function_arg1, function_arg2):
        print(*args, **kwargs)
        func(function_arg1, function_arg2)

    return wrap


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
