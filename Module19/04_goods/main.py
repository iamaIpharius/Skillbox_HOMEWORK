goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def total_cost(key, store, goods):
    id_of_good = goods[key]
    total_ad = 0
    total_price = 0
    if id_of_good in store:
        for position in store[id_of_good]:
            total_ad += position['quantity']
            total_price += position['quantity'] * position['price']
    print('{good} - {ad} шт, стоимость {total_price} руб'.format(good=key, ad=total_ad, total_price=total_price))
    return total_price


for item in goods:
    total_cost(item, store, goods)
