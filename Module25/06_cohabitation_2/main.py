import random


class House:
    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__catFood = 30
        self.__dirt = 0
        self.__money_index = 0
        self.__food_index = 0
        self.__coat_index = 0

    def get_money(self):
        return self.__money

    def get_food(self):
        return self.__food

    def get_catFood(self):
        return self.__catFood

    def get_dirt(self):
        return self.__dirt

    def set_money(self, index):
        self.__money += index


    def set_food(self, index):
        self.__food += index


    def set_catFood(self, index):
        self.__catFood += index

    def set_dirt(self, index):
        self.__dirt += index

    def set_coat_index(self):
        self.__coat_index += 1

    def set_money_index(self, index):
        self.__money_index += index

    def set_food_index(self, index):
        self.__food_index += index

    def info(self):
        print(f'Деняк в доме {self.__money}')
        print(f'Еды в доме {self.__food}')
        print(f'Кошачей еды в доме {self.__catFood}')
        print(f'Грязи в доме {self.__dirt}')

    def year_info(self):
        print(f'Заработано {self.__money_index}')
        print(f'Съедено {self.__food_index}')
        print(f'Куплено шуб {self.__coat_index}')


class Creature:
    def __init__(self, name, house):
        self.__name = name
        self.__feed = 30
        self.__house = house
        self.__alive = True

    def eat(self):
        index = random.randint(1, 30)
        self.set_feed(index)
        self.get_house().set_food(-index)
        self.get_house().set_food_index(index)

    def info(self):
        if self.__alive:
            print(f'{self.__name} жив, сытость: {self.__feed}')
        else:
            print(self.__name, 'Умер')

    def set_feed(self, index):
        self.__feed += index
        if self.__feed > 100:
            self.__feed = 100

    def get_feed(self):
        return self.__feed
    def get_house(self):
        return self.__house

    def get_alive(self):
        return self.__alive

    def set_alive(self, index):
        self.__alive = index

    def act(self):
        if self.__feed <= 0:
            self.__alive = False
        elif not self.__alive:
            return
        self.eat()


class Human(Creature):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.__happiness = 100

    def set_happiness(self, index):
        self.__happiness += index
        if self.__happiness > 100:
            self.__happiness = 100

    def pet_the_cat(self):
        self.set_happiness(5)

    def info(self):
        super().info()
        print(f'Счастье: {self.__happiness}')

    def act(self):
        super(Human, self).act()
        if self.__happiness <= 10:
            self.set_alive(False)
        if self.get_house().get_dirt() >= 90:
            self.set_happiness(-10)


class Cat(Creature):
    def __init__(self, name, house):
        super().__init__(name, house)

    def eat(self):
        index = random.randint(1, 10)
        self.get_house().set_catFood(-index)
        self.set_feed(2 * index)
        if self.get_feed() > 100:
            self.set_feed(100)

    def damage_house(self):
        index = random.randint(1, 10)
        if index == 1:
            self.get_house().set_dirt(5)

    def act(self):
        if self.get_feed() <= 0:
            self.set_alive(False)
        elif not self.get_alive():
            return
        self.damage_house()
        self.eat()


class HumanRoleModel1(Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def play(self):
        self.set_feed(-10)
        self.set_happiness(20)

    def work(self):
        self.set_feed(-10)
        self.get_house().set_money(150)
        self.get_house().set_money_index(150)

    def act(self):
        super(HumanRoleModel1, self).act()
        self.work()
        self.eat()
        self.pet_the_cat()
        self.play()


class HumanRoleModel2(Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def buy_products(self):
        self.set_feed(-10)
        self.get_house().set_food(10)
        self.get_house().set_catFood(10)
        self.get_house().set_money(-20)

    def buy_coat(self):
        self.set_feed(-10)
        self.get_house().set_money(-350)
        self.set_happiness(60)
        self.get_house().set_coat_index()

    def clean(self):
        index = random.randint(1, 100)
        self.set_feed(-10)
        self.get_house().set_dirt(-index)

    def act(self):
        super(Human, self).act()
        if self.get_house().get_food() <= 10 or self.get_house().get_catFood() <= 10:
            self.buy_products()
        if self.get_house().get_dirt() >= 50:
            self.clean()
        self.eat()
        self.pet_the_cat()
        if self.get_house().get_money() > 500:
            self.buy_coat()


my_house = House()
biba = HumanRoleModel1('Biba', my_house)
boba = HumanRoleModel2('Boba', my_house)
lupa = Cat('Lupa', my_house)


for i in range(1, 366):
    print(f'\n {i} День \n')
    my_house.set_dirt(5)
    lupa.damage_house()
    lupa.act()
    lupa.info()
    biba.act()
    biba.info()
    boba.act()
    boba.info()

my_house.year_info()

