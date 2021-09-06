from collections.abc import Iterable


class Squares:
    def __init__(self, number: int) -> None:
        self.__number = number
        self.__counter = 0

    def __iter__(self) -> Iterable[int]:
        self.__counter = 0
        return self

    def __next__(self) -> int:
        if self.__counter >= self.__number:
            raise StopIteration()
        self.__counter += 1
        return self.__counter ** 2


def sq_gen(number: int) -> Iterable[int]:
    for i in range(1, number + 1):
        yield i ** 2


my_number = int(input('Введите число: '))

for i in Squares(my_number):
    print(i, end=' ')
print()
for i in sq_gen(my_number):
    print(i, end=' ')

print()

my_gen = (i ** 2 for i in range(1, my_number + 1))
for i in my_gen:
    print(i, end=' ')
