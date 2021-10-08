from collections.abc import Callable
import functools
from datetime import datetime


# def logger(form):
#     def dec(func):
#         @functools.wraps(func)
#         def wrap(*args, **kwargs):
#             dtm = datetime.utcnow()
#             temp = form.replace('b', str(dtm.month))
#             temp = temp.replace('d', str(dtm.day))
#             temp = temp.replace('Y', str(dtm.year))
#             temp = temp.replace('H', str(dtm.hour))
#             temp = temp.replace('M', str(dtm.minute))
#             result = temp.replace('S', str(dtm.second))
#             f = func(*args, **kwargs)
#             print(f'метод {func} класса выполнен {result}')
#             return f
#
#         return wrap
#
#     return dec


def log_methods(form):
    @functools.wraps(form)
    def dec(cls):

        for i_method in dir(cls):
            if not i_method.startswith('__'):
                dtm = datetime.utcnow()
                temp = form.replace('b', str(dtm.month))
                temp = temp.replace('d', str(dtm.day))
                temp = temp.replace('Y', str(dtm.year))
                temp = temp.replace('H', str(dtm.hour))
                temp = temp.replace('M', str(dtm.minute))
                result = temp.replace('S', str(dtm.second))
                print(f'метод {i_method} класса {cls.__name__} выполнен {result}')

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

