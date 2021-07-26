import random


class Warrior:
    def __init__(self, name, hp=100, hit=20):
        self.name = name
        self.hp = hp
        self.hit = hit

    def defence(self):
        self.hp -= self.hit
        print(f'У война по имени {self.name} осталось здоровья - {self.hp}\n')
        if self.hp <= 0:
            print(f'Бравый воин по имени {self.name} погиб!\n')

    def attack(self, target):
        target.defence()




warrior_1 = Warrior('Boba')
warrior_2 = Warrior('Biba')

fighting_start = True
print('Бой начался!\n')
while fighting_start:
    attacker = random.randint(1, 2)
    if warrior_1.hp > 0 and warrior_2.hp > 0:

        if attacker == 1:
            print(f'Воин по имени {warrior_1.name} наносит сокрушительный удар войну по имени {warrior_2.name}')
            warrior_1.attack(warrior_2)
        else:
            print(f'Воин по имени {warrior_2.name} наносит сокрушительный удар войну по имени {warrior_1.name}')
            warrior_2.attack(warrior_1)
    elif warrior_1.hp <= 0:
        print(f'Бой окончен\nПобедил {warrior_2.name}!')
    else:
        print(f'Бой окончен\nПобедил {warrior_1.name}!')
        fighting_start = False
