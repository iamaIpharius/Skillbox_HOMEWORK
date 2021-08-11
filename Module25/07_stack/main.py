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
    def __init__(self, stack):
        self.__stack = stack

    def __str__(self):
        temp = self.__stack.get_list()
        temp = sorted(temp, key=lambda task: task[1])
        new_temp = []
        for i_elem in temp:
            if i_elem[1] not in new_temp:
                new_temp.append(i_elem[1])
            new_temp.append(i_elem[0])

        new_temp = [str(i) for i in new_temp]
        result = ' '.join(new_temp)
        return result

    def new_task(self, task, priority):
        new_task = (task, priority)
        self.__stack.add(new_task)

    def delete_task(self, task):
        list = self.__stack.get_list()
        for index, val in enumerate(list):
            for elem in val:
                if task == elem:
                    list.pop(index)
                    self.__stack.set_list(list)
                    break
        else:
            print('Элемент для удаления не найден')





my_stack = Stack()
task_manager = Manager(my_stack)

task_manager.new_task('купить продукты', 2)
task_manager.new_task('сделать дз', 3)
task_manager.new_task('работать', 1)
task_manager.new_task('есть', 1)

print(task_manager)

task_manager.delete_task('есть')

print(task_manager)