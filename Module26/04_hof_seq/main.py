from typing import List
class QHofstadter:
    def __init__(self, s: List[int]) -> None:
        self.s = s

    def __next__(self) -> int:
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> None:
        return self


my_q = QHofstadter([1, 1])
a = [next(my_q) for _ in range(10)]
print(a)
