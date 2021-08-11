import math


class Car:
    name = 'Автомобиль'

    def __init__(self, x, y, direction):
        self.__x = x
        self.__y = y
        if direction > 360 or direction < 0:
            raise ValueError
        else:
            self.__dir = direction

    def move(self, distance):
        dir_rad = math.radians(self.__dir)
        x2 = distance * math.cos(dir_rad)
        y2 = distance * math.sin(dir_rad)
        self.__x = self.__x + x2
        self.__y = self.__y + y2
        print(
            f'{self.name} проехал {distance} километров и оказался в точке {round(self.__x, 1)}, {round(self.__y, 1)}')

    def change_dir(self, new_dir):
        self.__dir = new_dir


class Bus(Car):
    name = 'Автобус'

    def __init__(self, x, y, direction, passengers):
        super().__init__(x, y, direction)
        self.__pas = passengers
        self.__money = 0

    def move(self, distance):
        super().move(distance)
        self.__money += (1 * self.__pas * distance)

    def enter(self, passengers):
        self.__pas += passengers

    def exit(self, passengers):
        self.__pas -= passengers
        if self.__pas < 0:
            self.__pas = 0


    def info(self):
        print(f'Количество пассажиров {self.__pas}')
        print(f'Количество деняк {self.__money}')



my_car = Car(0, 0, 45)
my_car.move(50)
my_car.change_dir(73)
my_car.move(50)

my_bus = Bus(0, 0, 45, 10)
my_bus.info()
my_bus.move(15)
my_bus.info()
my_bus.enter(5)
my_bus.change_dir(155)
my_bus.move(5)
my_bus.info()
my_bus.exit(2)
my_bus.info()
my_bus.enter(6)
my_bus.info()
my_bus.move(15)
my_bus.info()
