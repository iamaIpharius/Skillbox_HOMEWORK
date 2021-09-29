import datetime
import functools
from typing import Callable, Any


def logging(f: Callable) -> Any:
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
        print('*' * 5)
        print(f'Название функции - {f.__name__}')
        print(f.__doc__)
        try:
            f(*args, **kwargs)
        except Exception as ex:
            template = "{0} Обнаружена ошибка типа {1} в функции {2}. Аргументы: {3}\n"
            dtm = datetime.datetime.now()
            message = template.format(dtm, type(ex).__name__, f.__name__, ex.args)
            print(message)
            with open('function_errors.log', 'a') as log:
                log.write(message)
        return

    return wrapper


@logging
def test(a: int, b: int) -> int:
    """
    Тестовая функция
    :return: возвращает сумму a + b
    """

    result = a + b
    print(f'Результат выполнения тестовой функции {result}\n')
    return result


test(1, 2)
test(1, 'b')
test(1, 11)
