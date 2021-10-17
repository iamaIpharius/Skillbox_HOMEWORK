import re

numbers = ['9999999999', '999999-999', '99999x9999']

pattern = r'\b[89]\d{9}\b'

for i, number in enumerate(numbers, 1):
    if re.search(pattern, number):
        print(f'{i} номер: в порядке')
    else:
        print(f'{i} номер: не подходит')