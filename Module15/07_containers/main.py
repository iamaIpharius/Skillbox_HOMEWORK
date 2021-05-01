n = int(input('Введите количество контейнеров: '))
container_list = []
for _ in range(n):
    container_weight = int(input('Введите вес контейнера: '))
    while container_weight > 200:
        container_weight = int(input('Введите вес контейнера не превышающий 200: '))
    container_list.append(container_weight)

new_container_weight = int(input('Введите вес нового контейнера: '))
while new_container_weight > 200:
    new_container_weight = int(input('Введите вес нового контейнера не превышающий 200: '))
position = 0
for i_cont in range(len(container_list)):
    if container_list[i_cont] < new_container_weight:
        position = i_cont
        break
print('Номер, куда встанет новый контейнер:', position + 1)