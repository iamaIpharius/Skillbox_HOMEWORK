from collections.abc import Callable
import functools

app = dict()


def callback(path: str):
    def dec(func: Callable) -> Callable:
        app[path] = func
        
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            
            return func(*args, **kwargs)

        return wrap

    return dec


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


example()
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
