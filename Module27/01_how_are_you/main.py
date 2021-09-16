import time, random, functools
from typing import Callable, Any


def how_are_you(f: Callable) -> Callable:
    """
    Декоратор. Задает назойливый вопрос
    :param f: передается функция
    :return: возвращает функцию
    """
    input('Как дела?')
    print('А у меня не очень!\nЛадно, держи свою функцию...')
    return f


@how_are_you
def test() -> None:
    """
    Тестовая функция
    :return: печатает в консоль что-то
    """
    print('<Тут что-то происходит...>')


test()
