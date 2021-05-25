count_of_protocol = int(input('Сколько записей в протоколе? '))
result_dict = dict()
print('Введите записи (результат и имя):')
for i in range(1, count_of_protocol + 1):
    scribe = input('{0} запись: '.format(i))
    result = scribe.split()
    result_dict[i] = result

first_place_score = 0
first_place = []
for position, score in result_dict.items():
    if int(score[0]) > first_place_score:
        first_place_score = int(score[0])
        first_place = score

second_place_score = 0
second_place = []
for position, score in result_dict.items():
    if first_place_score >= int(score[0]) > second_place_score and score[1] != first_place[1]:
        second_place_score = int(score[0])
        second_place = score

third_place_score = 0
third_place = []
for position, score in result_dict.items():
    if second_place_score >= int(score[0]) > third_place_score and score[1] != first_place[1] and score[1] != \
            second_place[1]:
        third_place_score = int(score[0])
        third_place = score

print('1 место. {name} ({score})'.format(name=first_place[1], score=first_place[0]))
print('2 место. {name} ({score})'.format(name=second_place[1], score=second_place[0]))
print('3 место. {name} ({score})'.format(name=third_place[1], score=third_place[0]))

