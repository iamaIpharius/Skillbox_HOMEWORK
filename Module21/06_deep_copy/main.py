site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def get_new_sites(struct, key, name):
    if count == 0:
        return
    for s_key, s_item in struct.items():
        if isinstance(s_item, str):
            if key in s_item:
                temp = s_item.replace(key, name)
                struct[s_key] = temp
                return
            else:
                return
        elif isinstance(s_item, dict):
            get_new_sites(s_item, key, name)


def nice_print(struct, count=1):
    for s_key, s_value in struct.items():
        if isinstance(s_value, str):
            print('/'*count, s_key, ':', s_value)
        elif isinstance(s_value, dict):
            print('/'*count, s_key, ':')
            nice_print(s_value, count=count+1)


count = int(input('Сколько будет сайтов? '))

for _ in range(count):
    old = input('Введите название старого продукта: ')
    new = input('Введите название нового продукта: ')
    get_new_sites(site, old, new)
    print(site)
    nice_print(site)
