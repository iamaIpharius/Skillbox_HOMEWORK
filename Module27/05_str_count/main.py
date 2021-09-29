import datetime
import functools
from typing import Callable, Any


def counter(f: Callable) -> Any:
    """

    :param f: декорируемая функция
    :return: оберточная функция
    """

    @functools.wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """

        :param args: аргументы
        :param kwargs: именованные аргументы
        :log: файл для подсчета количества вызовов функции
        :f: декорируемая функция выполняется
        :return: конец
        """
        with open('openlog.txt', 'a') as log:
            dtm = datetime.datetime.now()
            log.write(f'function execute {dtm} \n')
        with open('openlog.txt', 'r') as log:
            count = sum(1 for _ in log)

        print(f'Функция вызвана {count} раз')
        return f(*args, **kwargs)

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
