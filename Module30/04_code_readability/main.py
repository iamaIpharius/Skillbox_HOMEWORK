from typing import List

print([x for x in range(1, 1001)]) #однострочное решение

result: List = [] #простое решение
for count in range(1, 1001):
    result.append(count)
print(result)
