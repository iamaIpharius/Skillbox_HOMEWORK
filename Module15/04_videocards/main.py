cards_n = int(input('Введите количество видеокарт: '))
cards_list = []
new_cards_list = []
for i in range(cards_n):
    print(i + 1, 'Видеокарта', end=' ')
    card = int(input())
    cards_list.append(card)

coolest_card = cards_list[0]

for i in range(cards_n):
    if cards_list[i] > coolest_card:
        coolest_card = cards_list[i]

for i in range(cards_n):
    if cards_list[i] != coolest_card:
        new_cards_list.append(cards_list[i])

print('Старый список видеокарт:', cards_list)
print('Новый список видеокарт:', new_cards_list)