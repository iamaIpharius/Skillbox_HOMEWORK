import random


class Warrior:
    def __init__(self, name, hp=100, hit=20):
        self.name = name
        self.hp = hp
        self.hit = hit

    def recieve_hit(self):
        self.hp -= self.hit
        print(f'У война по имени {self.name} осталось здоровья - {self.hp}\n')
        if self.hp <= 0:
            print(f'Бравый воин по имени {self.name} погиб!\n')


warrior_1 = Warrior('Boba')
warrior_2 = Warrior('Biba')

fighting_start = True
print('Бой начался!\n')
while fighting_start:
    who_is_receiving_dmg = random.randint(1, 2)
    if warrior_1.hp > 0 and warrior_2.hp > 0:

        if who_is_receiving_dmg == 1:
            print(f'Воин по имени {warrior_2.name} наносит сокрушительный удар войну по имени {warrior_1.name}')
            warrior_1.recieve_hit()
        else:
            print(f'Воин по имени {warrior_1.name} наносит сокрушительный удар войну по имени {warrior_2.name}')
            warrior_2.recieve_hit()
    elif warrior_1.hp <= 0:
        print(f'Бой окончен\nПобедил {warrior_2.name}!')
    else:
        print(f'Бой окончен\nПобедил {warrior_1.name}!')
        fighting_start = False
