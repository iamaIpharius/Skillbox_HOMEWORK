def get_family_members(family_dict, surname):
    for name, age in family_dict.items():
        if name.startswith(surname):
            print(name, age)


my_dict = {'Cидорова Анна': 23, "Иванова Лена": 22, "Петрова Катя": 55}

surname = input('Введите фамилию: ')

get_family_members(my_dict, surname)
