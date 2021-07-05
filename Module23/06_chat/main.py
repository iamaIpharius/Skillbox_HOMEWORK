
user_name = input('Приветствуем в чате! Введите свое имя: ')
while True:
    try:
        act = input('Посмотреть текущий текст чата (0) или Отправить сообщение(1)? ')
        if act == '0':
            with open('chat.txt', 'r', encoding='utf-8') as chat_file:
                for line in chat_file:
                    print(line)
        elif act == '1':
            with open('chat.txt', 'a', encoding='utf-8') as chat_file:
                message = input('Введите свое сообщение: ')
                chat_file.write(user_name + ':' + '\n')
                chat_file.write(('\t' + message + '\n'))
        else:
            raise ValueError
    except ValueError:
        print('Попробуйте еще раз')
