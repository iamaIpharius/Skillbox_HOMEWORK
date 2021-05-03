roll_list = []
human_foot_list = []

N = int(input('Сколько коньков? '))
K = int(input('Сколько людей?'))

match_ad = 0
for i in range(N):
    print('Размер', i + 1, 'пары:', end=' ')
    roll_list.append(int(input()))
for i in range(K):
    print('Размер ноги', i + 1, 'человека:', end=' ')
    human_foot_list.append(int(input()))

roll_list.sort()
human_foot_list.sort()

for roll in roll_list:
    for foot in human_foot_list:
        if foot <= roll:
            match_ad += 1
            roll_list.remove(roll)
            human_foot_list.remove(foot)
print('Наибольшее кол-во людей, которые могут взять ролики:', match_ad)