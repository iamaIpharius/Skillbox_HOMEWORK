shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

item_req = input('Название детали: ')
item_ad = 0
item_sum = 0
for position in shop:
        if position[0] == item_req:
                item_ad += 1
                item_sum += position[1]

print('Кол-во деталей -', item_ad)
print('Общая стоимость -', item_sum)