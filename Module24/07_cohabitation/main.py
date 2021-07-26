import random


class Flat:
    def __init__(self):
        self.fridge = 50
        self.money = 0


class Human:

    def __init__(self, name, flat):
        self.name = name
        self.feed = 50
        self.my_flat = flat
        self.alive = True

    def eating(self, index):
        if self.alive:
            self.feed += index
            self.my_flat.fridge -= index
        else:
            print(f'{self.name} Мертв!')

    def working(self, index):
        if self.alive:
            self.feed -= index
            self.my_flat.money += index
            if self.feed <= 0:
                self.alive = False
                print(f'{self.name} умер от голода!')
        else:
            print(f'{self.name} Мертв!')

    def playing(self, index):
        if self.alive:
            self.feed -= index
            if self.feed <= 0:
                self.alive = False
                print(f'{self.name} умер от голода!')
        else:
            print(f'{self.name} Мертв!')

    def buying_food(self, index):
        if self.alive:
            self.my_flat.money -= index
            self.my_flat.fridge += index
        else:
            print(f'{self.name} Мертв!')

    def info(self):
        print(f'{self.name}')
        print('Сытость -', self.feed)
        print('Еды в запасе -', self.my_flat.fridge)
        print('Деняк -', self.my_flat.money)

    def act(self):
        dice = random.randint(1, 6)
        index = 5
        if self.feed <= 20:
            self.eating(index)
        elif self.my_flat.fridge <= 10:
            self.buying_food(index)
        elif self.my_flat.money <= 50:
            self.working(index)
        elif dice == 1:
            self.working(index)
        elif dice == 2:
            self.eating(index)
        else:
            self.playing(index)
        self.info()


house = Flat()
people = [Human('Biba', house), Human('Boba', house)]

for i in range(1, 366):
    print(f'{i} день совместной жизни!')
    for human in people:
        human.act()

for human in people:
    human.info()
