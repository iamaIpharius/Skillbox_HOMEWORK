friends_ad = int(input('Сколько друзей? '))
friends_list = []
for friend_num in range(1, friends_ad + 1):
    friends_list.append(0)


deb_ad = int(input('Сколько расписок? '))

for deb in range(1, deb_ad + 1):
    print(deb, 'расписка')
    to_friend = int(input('Кому? '))
    from_friend = int(input('От кого? '))
    money = int(input('Сколько? '))

    friends_list[to_friend - 1] += money
    friends_list[from_friend - 1] += -money

print('Баланс друзей: ')
for friend in range(len(friends_list)):
    print(friend + 1, ':', friends_list[friend])
