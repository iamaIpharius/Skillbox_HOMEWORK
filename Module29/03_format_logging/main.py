from collections.abc import Callable
import functools
from datetime import datetime
import time


def logger(_func=None, *, form: str):
    def dec(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            dtm = datetime.utcnow()
            temp = form.replace('b', str(dtm.month))
            temp = temp.replace('d', str(dtm.day))
            temp = temp.replace('Y', str(dtm.year))
            temp = temp.replace('H', str(dtm.hour))
            temp = temp.replace('M', str(dtm.minute))
            result = temp.replace('S', str(dtm.second))
            print(f'---Запускается метод {func}, время запуска: {result}')
            start = time.time()
            f = func(*args, **kwargs)
            end = time.time()
            time_result = round(end - start, 3)
            print(f'---Завершение {func}, время работы {time_result}')
            return f

        return wrap

    if _func is None:
        return dec
    else:
        return dec(_func)


def log_methods(form: str):
    def dec(cls: Callable) -> Callable:

        for i_method in dir(cls):
            if not i_method.startswith('__'):
                cur_method = getattr(cls, i_method)
                dec_method = logger(_func=cur_method, form=form)
                setattr(cls, i_method, dec_method)

        return cls

    return dec


@log_methods("b d Y - H:M:S")
class A:

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result




my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
