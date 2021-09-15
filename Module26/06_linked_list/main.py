from typing import Any
from typing import Iterable


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.counter = 0

    def __str__(self) -> str:
        print('[', end='')
        if self.head is None:
            return ']'
        else:
            cur = self.head
            while cur:
                print(str(cur.data), end=' ')
                cur = cur.next_node
            return ']'

    def __next__(self) -> Iterable[Any]:
        if self.counter <= self.len():
            cur = self.get(self.counter)
            self.counter += 1
            return cur
        else:
            raise StopIteration

    def __iter__(self) -> Iterable[Any]:
        self.counter = 0
        return self

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next_node:
                cur = cur.next_node
            cur.next_node = new_node

    def len(self) -> int:
        i = 0
        cur = self.head
        if cur:
            while cur.next_node:
                cur = cur.next_node
                i += 1
            else:
                return i
        else:
            raise ValueError

    def get(self, index: int) -> Any:
        i = 0
        cur = self.head
        if cur:
            while index != i:
                if cur.next_node:
                    cur = cur.next_node
                    i += 1
                else:
                    raise BaseException
            return cur.data
        else:
            raise BaseException

    def remove(self, index: int) -> None:
        i = 0
        cur = self.head
        cur_prev = None
        while index != i:
            cur_prev = cur
            cur = cur.next_node
            i += 1
        if index == 0:
            self.head = cur.next_node
        else:
            cur = cur.next_node
            cur_prev.next_node = cur


try:
    my_list = LinkedList()

    my_list.append(10)
    my_list.append('fffff')
    my_list.append(30)
    print('Текущий список:', my_list)

    for i in my_list:
        print(i)
    print('Текущий список:', my_list)
    print(my_list.get(1))
    my_list.remove(0)
    print('Текущий список:', my_list)
except BaseException:
    print('Запрашиваемый индекс больше чем количество элементов в списке')
except ValueError:
    print('Список пуст')
