class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning
        elif isinstance(other, Water):
            return Steam
        elif isinstance(other, Earth):
            return Lava
        elif isinstance(other, Mud):
            return Brick


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm
        elif isinstance(other, Fire):
            return Lightning
        elif isinstance(other, Earth):
            return Dust

class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud
        elif isinstance(other, Fire):
            return Lava
        elif isinstance(other, Air):
            return Dust

class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm
        elif isinstance(other, Fire):
            return Steam
        elif isinstance(other, Earth):
            return Mud

class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Mud:
    name = 'Грязь'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Brick

class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Огонь'

class Brick:
    name = 'Кирпич'

a = Fire()
b = Mud()
c = a + b

print(c.name)
