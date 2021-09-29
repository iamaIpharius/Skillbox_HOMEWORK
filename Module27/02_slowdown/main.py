import time, random, functools
from typing import Callable, Any

def wait(f: Callable) -> Any:
    """

    :param f: декорируемая функция
    :return: оберточная функция
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """

        :param args: аргументы
        :param kwargs: именованные аргументы
        :f: декорируемая функция выполняется
        :return: конец
        """
        time.sleep(5)
        result = f(*args, **kwargs)
        return result
    return wrapper

@wait
def test() -> None:
    """
    Тестовая функция
    :return: печатает в консоль что-то
    """
    print('<Тут что-то происходит...>')


test()
