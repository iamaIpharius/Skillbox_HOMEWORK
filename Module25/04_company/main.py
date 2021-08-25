class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age



class Employee(Person):
    def salary(self):
        pass


class Manager(Employee):
    def salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def salary(self):
        return 5000 + self.__sales / 100 * 5


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours

    def salary(self):
        return 100 * self.__hours


employees = [
    Manager('Иван', 'Иванов', 22),
    Manager('Василий', 'Иванов', 23),
    Manager('Петр', 'Петров', 25),
    Agent('Герман', 'Кеков', 25, 500),
    Agent('Виталий', 'Васильев', 52, 600),
    Agent('Петр', 'Громов', 33, 580),
    Worker('Иван', 'Калашников', 87, 160),
    Worker('Максим', 'Котов', 55, 170),
    Worker('Константин', 'Максимов', 21, 180)
]

for emp in employees:
    print(emp.salary())