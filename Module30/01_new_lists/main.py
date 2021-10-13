from typing import List
import functools

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


result_floats = list(map(lambda x: round(x ** 3, 3), floats))
result_names = list(filter(lambda x: len(x) >= 5, names))
result_numbers = functools.reduce(lambda a, b: a * b, numbers)
print(result_floats, result_names, result_numbers)
