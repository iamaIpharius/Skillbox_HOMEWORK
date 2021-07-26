class Winer:
    def __init__(self, field):
        self.field = field



class Cell:
    def __init__(self, number):
        self.number = number
        self.value = str(number)



class Field:
    def __init__(self):
        self.field_list = {i: Cell(i) for i in range(1, 10)}

    def show(self):
        num_index = 1
        for _ in range(3):
            for _ in range(3):
                print(self.field_list[num_index].value, end=' ')
                num_index += 1
            print(' ')
        print('\n')

    def move(self, value, number):
        self.field_list[number].value = value
        self.show()

    def checking(self):
        if self.field_list[1].value == self.field_list[2].value == self.field_list[3].value:
            print(f'Победили {self.field_list[1].value}')
            return False
        elif self.field_list[4].value == self.field_list[5].value == self.field_list[6].value:
            print(f'Победили {self.field_list[4].value}')
            return False
        elif self.field_list[7].value == self.field_list[8].value == self.field_list[9].value:
            print(f'Победили {self.field_list[7].value}')
            return False
        elif self.field_list[1].value == self.field_list[4].value == self.field_list[7].value:
            print(f'Победили {self.field_list[1].value}')
            return False
        elif self.field_list[2].value == self.field_list[5].value == self.field_list[8].value:
            print(f'Победили {self.field_list[2].value}')
            return False
        elif self.field_list[3].value == self.field_list[6].value == self.field_list[9].value:
            print(f'Победили {self.field_list[3].value}')
            return False
        elif self.field_list[1].value == self.field_list[5].value == self.field_list[9].value:
            print(f'Победили {self.field_list[1].value}')
            return False
        elif self.field_list[3].value == self.field_list[5].value == self.field_list[7].value:
            print(f'Победили {self.field_list[3].value}')
            return False
        for value in self.field_list.values():
            if value.value.isdigit():

                break

        else:
            print('Ничья!')
            return False
        return True

    def play(self):
        playing = True
        self.show()
        x = True
        o = False
        while playing:
            if x:
                choice = int(input('Введите номер ячейки, куда поставить Х: '))
                self.move('x', choice)
                x = False
                o = True
            elif o:
                choice = int(input('Введите номер ячейки, куда поставить О: '))
                self.move('o', choice)
                x = True
                o = False
            playing = self.checking()


my_field = Field()
my_field.play()
