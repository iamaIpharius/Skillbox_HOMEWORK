import timeit


res: float = timeit.timeit('"".join(str(n) for n in range(100))', number=10000)
res1: float = timeit.timeit("''.join([str(a) for a in range(100)])", number=10000)
res2: float = timeit.timeit("''.join(map(lambda x: str(x), range(100)))", number=10000)


print(res)
print(res1)
print(res2)

