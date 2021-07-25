class Parent:
    list_of_children = []

    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        for arg in args:
            if isinstance(arg, Child):
                self.list_of_children.append(arg)
            else:
                raise ValueError
            if age - arg.age < 16:
                print(f'Разница между родителем и ребенком {arg.name} менее 16 лет!')
                raise ArithmeticError

    def info(self):
        print(self.name)
        print(self.age)
        for child in self.list_of_children:
            print(child.name)
        print('\n')

    def calming_child(self, child):
        if child in self.list_of_children:
            if child.is_calm:
                print('Ребенок уже спокоен')
            else:
                child.is_calm = True
                print('Ребенок успокоен')
        else:
            print('Это не наш ребенок')

    def feed_the_child(self, child):
        if child in self.list_of_children:
            if child.is_not_hungry:
                print('Ребенок уже сыт')
            else:
                child.is_not_hungry = True
                print('Ребенок накормлен')
        else:
            print('Это не наш ребенок')


class Child:

    def __init__(self, name, age, is_calm, is_not_hungry):
        self.name = name
        self.age = age
        if isinstance(is_calm, bool) and isinstance(is_not_hungry, bool):
            self.is_calm = is_calm
            self.is_not_hungry = is_not_hungry
        else:
            raise ValueError

    def info(self):
        print(self.name, self.age, self.is_calm, self.is_not_hungry)



try:
    child_1 = Child('Masha', 10, True, True)
    child_2 = Child('Vano', 11, False, True)
    child_3 = Child('Dasha', 16, False, False)
    child_4 = Child('Rasha', 5, True, False)
    parent_1 = Parent('Biba', 38, child_1, child_2, child_3)
    parent_1.info()

    children = [child_1, child_2, child_3, child_4]
    for child in children:
        child.info()
        parent_1.calming_child(child)
        parent_1.feed_the_child(child)
        child.info()
        print('\n')

except ValueError:
    print('Это не ребенок!')
except ArithmeticError:
    print('Неподходящий возраст')
