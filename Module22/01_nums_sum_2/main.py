file = open('numbers.txt', 'r')

result = 0
for i in file:
    for j in i:
        if j == '2':
            result += 2
print(result)
answer = open('answer.txt', 'w')
answer.write(str(result))
file.close()
answer.close()

