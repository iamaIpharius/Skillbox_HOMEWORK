def get_family_members(family_dict, surname):

    for name, age in family_dict.items():
        if name.lower().startswith(surname.lower()):
            print(name, age)
        elif name.lower().startswith(surname[:-1].lower()):
            print(name, age)



my_dict = {
    'Сидорова Анна': 23,
    'Иванова Лена': 22,
    'Петрова Катя': 55,
    'Сидоров Иван': 23,
    'Сидорова Катя': 23,
    'Сидорович Анна': 23
}

surname = input('Введите фамилию: ')

get_family_members(my_dict, surname)
