import functools
from typing import Callable, Any


def counter(f: Callable) -> Any:
    """

    :param f: декорируемая функция
    :wrapper.count: атрибут для подсчета количества вызовов функции
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

        wrapper.count += 1
        result = f(*args, **kwargs)
        print(f'Функция выполнена {wrapper.count} раз')
        return result

    wrapper.count = 0


    return wrapper


@counter
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
print(greeting(name="Катя", age=16))
