guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
party_process = True
while party_process:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    is_this_new_guest = input('Гость пришел или ушел? ')

    if is_this_new_guest == 'пришел':
        guest_name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет,', guest_name, '!')
            guests.append(guest_name)
        else:
            print('Прости,', guest_name, 'мест нет')
    elif is_this_new_guest == 'ушел':
        guest_name = input('Имя гостя: ')
        if len(guests) == 0:
            print('Никого и так не осталось')
        else:
            print('Пока,', guest_name, '!')
            guests.remove(guest_name)
    elif is_this_new_guest == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        party_process = False
    else:
        print('Непонятно...')