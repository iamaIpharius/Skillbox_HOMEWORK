import random


class Flat:
    fridge = 50
    money = 0


class Human:
    alive = True

    def __init__(self, name, Flat):
        self.name = name
        self.feed = 50
        self.my_flat = Flat

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

house = Flat
people = [Human('Biba', house), Human('Boba', house)]


for i in range(1, 366):
    print(f'{i} день совместной жизни!')
    for human in people:

        dice = random.randint(1, 6)
        index = 5
        if human.feed <= 20:
            human.eating(index)
        elif human.my_flat.fridge <= 10:
            human.buying_food(index)
        elif human.my_flat.money <= 50:
            human.working(index)
        elif dice == 1:
            human.working(index)
        elif dice == 2:
            human.eating(index)
        else:
            human.playing(index)
        human.info()

for human in people:
    human.info()






