class Property:
    def __init__(self, worth):
        self.worth = worth

    def check(self, prop):
        if isinstance(prop, Apartment):
            return self.worth / 1000
        elif isinstance(prop, Car):
            return self.worth / 200
        elif isinstance(prop, CountryHouse):
            return self.worth / 500


class Apartment(Property):
    def __init__(self, worth):
        self.worth = worth

    def __str__(self):
        return 'Квартира'


class Car(Property):
    def __init__(self, worth):
        self.worth = worth

    def __str__(self):
        return 'Машина'


class CountryHouse(Property):
    def __init__(self, worth):
        self.worth = worth

    def __str__(self):
        return 'Дача'


money = int(input('Введите сколько у Вас деняк: '))
my_prop = [
    Apartment(int(input('Введите стоимость квартиры: '))),
    Car(int(input('Введите стоимость машины: '))),
    CountryHouse(int(input('Введите стоимость дачи: ')))
]
total_tax = 0
for item in my_prop:
    tax = item.check(item)
    total_tax += tax
    print(f'Налог на {item} составляет {tax}')

print(f'Общий налог = {total_tax}')

if money < total_tax:
    print('У Вас не хватает деняк!')
else:
    print('У Вас хватает деняк')
