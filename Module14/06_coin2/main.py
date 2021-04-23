def coin_in_radius(point1, point2, radius):
    if point1**2 + point2**2 <= radius**2:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Радиус: '))

coin_in_radius(x, y, r)