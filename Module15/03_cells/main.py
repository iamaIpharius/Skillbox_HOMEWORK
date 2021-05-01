n = int(input('Введите количество клеток: '))
bad_cells_list = []

for cell in range(n):
    print('Введите эффективность', cell + 1, 'клетки: ', end='')
    cell_eff = int(input())
    if cell_eff < (cell + 1):
        bad_cells_list.append(cell_eff)

print('Неподходящие значения:', bad_cells_list)