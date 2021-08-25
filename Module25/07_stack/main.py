def sort_f(tup):
    return tup[1]


class Stack:
    def __init__(self):
        self.__list = []

    def add(self, elem):
        self.__list.insert(0, elem)

    def remove(self):
        self.__list.pop(0)

    def get_list(self):
        return self.__list

    def set_list(self, new_list):
        self.__list = new_list


class Manager:
    def __init__(self):
        self.__dict_of_stacks = dict()

    def __str__(self):
        list_k = list(self.__dict_of_stacks.keys())
        list_k.sort()
        for i in list_k:
            print(f'Приоритет {i}')
            if len(self.__dict_of_stacks[i].get_list()) > 0:
                for task in self.__dict_of_stacks[i].get_list():
                    print(f'Задача - {task[0]}')
            else:
                print('(EMPTY)')

        return ''

    def new_task(self, task, priority):
        new_task = (task, priority)
        if priority in self.__dict_of_stacks:
            self.__dict_of_stacks[priority].add(new_task)
        else:
            self.__dict_of_stacks[priority] = Stack()
            self.__dict_of_stacks[priority].add(new_task)

    def delete_task(self, task):
        delete_list = []
        for d_elem in self.__dict_of_stacks.values():
            for l_elem in d_elem.get_list():
                if l_elem[0] == task:
                    delete_elem = (l_elem[0], l_elem[1], d_elem.get_list().index(l_elem))
                    delete_list.append(delete_elem)

        if len(delete_list) == 1:
            self.__dict_of_stacks[delete_list[0][1]].get_list().pop(delete_list[0][2])
        elif len(delete_list) > 1:
            for index, elem in enumerate(delete_list, 1):
                print(f'Номер задачи {index} Название задачи {elem[0]}, приоритет {elem[1]}')
            answer = int(input('Какую задачу удаляем? Введите номер: '))
            for index, elem in enumerate(delete_list, 1):
                if answer == index:
                    self.__dict_of_stacks[elem[1]].get_list().pop(elem[2])

        else:
            print('Элемент для удаления не найден')


task_manager = Manager()

task_manager.new_task('купить продукты', 2)
task_manager.new_task('сделать дз', 3)
task_manager.new_task('работать', 1)
task_manager.new_task('есть', 1)
task_manager.new_task('есть', 2)
task_manager.new_task('есть', 3)
task_manager.new_task('есть', 4)

print(task_manager)

task_manager.delete_task('есть')

print(task_manager)
