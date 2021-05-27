def score_key(a):
    return a[1][0]*100000000 - a[1][1]

count_of_protocol = int(input('Сколько записей в протоколе? '))
score_table = dict()
print('Введите записи (результат и имя):')

for i in range(1, count_of_protocol + 1):
    scribe = input('{0} запись: '.format(i))
    result = scribe.split()
    result[0] = int(result[0])
    if result[1] in score_table:
        if result[0] > score_table[result[1]][0]:
            score_table[result[1]] = [result[0], i]
    else:
        score_table[result[1]] = [int(result[0]), i]
scores = list(score_table.items())

scores.sort(key=score_key, reverse=True)
for i in range(3):
    print('{place} место. {name} ({score})'.format(place=i+1, name=scores[i][0], score=scores[i][1][0]))