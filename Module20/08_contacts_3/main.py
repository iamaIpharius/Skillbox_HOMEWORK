def get_name_phone(dictionary, surname):
    for name, phone in dictionary.items():
        if name.lower().startswith(surname.lower()):
            print(name, phone)

contacts = {
    'иванов лул': 9218473562,
    'петров kek': 8412894892,
    'Джонс Papa': 38942389481,
    'Сидоров Uncle Tom': 8923489235782,
    'Кропоткин Mister Twister': 89464289682
}

while True:
    request = input('Поиск или Добавить? ')
    if request.lower() == 'поиск':
        name = input('Введите фамилию: ')
        print(get_name_phone(contacts, name))
    elif request.lower() == 'добавить':
        name = input('Введите фамилию и имя: ')
        phone_num = int(input('Введите номер телефона: '))
        if name in contacts:
            print('Контакт уже есть в книжке')
            print(contacts)
        else:
            contacts[name] = phone_num
            print(contacts)
    else:
        print('Команда не распознана')
