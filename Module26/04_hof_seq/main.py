class QHofstadter:
    def __init__(self, s):
        self.s = s

    def __next__(self):
        if self.right_numbers():
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def right_numbers(self) -> bool:
        return (self.s[0] == 1 and self.s[1] == 1)


my_q = QHofstadter([1, 1])
a = [next(my_q) for _ in range(10)]
print(a)
