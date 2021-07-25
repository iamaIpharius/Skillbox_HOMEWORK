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
def checking(field):
    if field.field_list[1].value == field.field_list[2].value == field.field_list[3].value:
        print(f'Победили {field.field_list[1].value}')
        return False
    elif field.field_list[4].value == field.field_list[5].value == field.field_list[6].value:
        print(f'Победили {field.field_list[4].value}')
        return False
    elif field.field_list[7].value == field.field_list[8].value == field.field_list[9].value:
        print(f'Победили {field.field_list[7].value}')
        return False
    elif field.field_list[1].value == field.field_list[4].value == field.field_list[7].value:
        print(f'Победили {field.field_list[1].value}')
        return False
    elif field.field_list[2].value == field.field_list[5].value == field.field_list[8].value:
        print(f'Победили {field.field_list[2].value}')
        return False
    elif field.field_list[3].value == field.field_list[6].value == field.field_list[9].value:
        print(f'Победили {field.field_list[3].value}')
        return False
    elif field.field_list[1].value == field.field_list[5].value == field.field_list[9].value:
        print(f'Победили {field.field_list[1].value}')
        return False
    elif field.field_list[3].value == field.field_list[5].value == field.field_list[7].value:
        print(f'Победили {field.field_list[3].value}')
        return False
    for value in field.field_list.values():
        if value.value.isdigit():
            break
    else:
        return False
    return True

my_field = Field()

playing = True
my_field.show()
x = True
o = False
while playing:
    if x:
        choice = int(input('Введите номер ячейки, куда поставить Х: '))
        my_field.move('x', choice)
        x = False
        o = True
    elif o:
        choice = int(input('Введите номер ячейки, куда поставить О: '))
        my_field.move('o', choice)
        x = True
        o = False
    playing = checking(my_field)