class Potato:
    states = {0:'Отсутствует', 1:'Росток', 2:'Зеленая', 3:'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

class Garden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела\n')
            return False
        else:
            print('Вся картошка созрела, можно собирать!')
            return True



class Gardener:
    harvest = []

    def __init__(self, name, count_of_plants_per_garden):
        self.name = name
        self.count_of_plants_per_garden = count_of_plants_per_garden
        self.my_garden = Garden(count_of_plants_per_garden)


    def gardening(self):
        self.my_garden.grow_all()

    def harvesting(self):
        if self.my_garden.are_all_ripe():
            print('Собираем урожай\n')
            for _ in range(self.count_of_plants_per_garden):
                self.harvest.append(self.my_garden.potatoes)
            self.my_garden.potatoes = []
        else:
            print('Подождем...\n')

    def seeding(self):

        if len(self.my_garden.potatoes) > 0:
            print('Подождите, на грядке не места')
        else:
            print('Картошка посажена!')
            self.my_garden = Garden(self.count_of_plants_per_garden)

    def info(self):
        print('Количество собраной картошки', len(self.harvest))
        print('На грядке картошки: ', len(self.my_garden.potatoes))



mister_gardener = Gardener('John', 5)
mister_gardener.my_garden.are_all_ripe()
for _ in range(3):
    mister_gardener.gardening()
    mister_gardener.my_garden.are_all_ripe()

mister_gardener.harvesting()
mister_gardener.info()
mister_gardener.seeding()
mister_gardener.my_garden.are_all_ripe()
mister_gardener.info()

for _ in range(3):
    mister_gardener.gardening()
    mister_gardener.my_garden.are_all_ripe()

mister_gardener.harvesting()
mister_gardener.info()
mister_gardener.seeding()
mister_gardener.seeding()