import functools
from typing import Callable, Any


def debug(f: Callable) -> Any:
    """

    :param f: декорируемая функция
    :return: оберточная функция
    """

    @functools.wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """

        :param args: аргументы
        :param kwargs: именованные аргументы
        :f: декорируемая функция выполняется
        :return: конец
        """
        all_arg = []
        if args:
            for i in args:
                all_arg.append(i)
        if kwargs:
            for key, value in kwargs.items():
                temp = f'{key}={value}'
                all_arg.append(temp)
        all_arg = tuple(all_arg)
        print(f'Вызывем функцию {f.__name__}{all_arg}')

        temp = f(*args, **kwargs)
        print(f'"{f.__name__}" вернула значение {temp}')
        return temp

    return wrapper


@debug
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
print(greeting(name="Катя", age=16))
