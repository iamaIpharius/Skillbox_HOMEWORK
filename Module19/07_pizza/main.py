number_of_orders = int(input('Сколько заказов? '))
order_dict = dict()

print('Введите слова через пробел в формате `Покупатель название пиццы количество заказанных пицц`: ')
for num in range(number_of_orders):
    order = input('{0} заказ: '.format(num + 1)).lower().split()  # Форма [Имя, Пицца, Кол-Во]
    name = order[0]
    pizza = order[1]
    total_piz = int(order[2])
    pizza_dict = dict()
    if name in order_dict:
        if pizza in order_dict[name]:
            order_dict[name][pizza] += total_piz
        else:
            pizza_dict[pizza] = total_piz
            order_dict[name].update(pizza_dict)
    else:
        pizza_dict[pizza] = total_piz
        order_dict[name] = pizza_dict

print(order_dict)
for item in sorted(order_dict.keys()):
    print(item.title(), ':')
    for order in sorted(order_dict[item]):
        print('\t', order.title(), ':', order_dict[item][order])
