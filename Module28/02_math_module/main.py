import math


class MyMath:
    """
    Модуль math в виде класса
    """
    @classmethod
    def circle_len(cls, radius):
        """
        Длина окружности круга
        :param radius: радиус
        :return:
        """
        return 2 * radius * math.pi

    @classmethod
    def circle_sq(cls, radius):
        """
        Площадь круга
        :param radius: радиус
        :return:
        """
        return (math.pi * radius) ** 2

    @classmethod
    def cube_sq(cls, side):
        """
        Объём куба
        :param side: сторона
        :return:
        """
        return side ** 3

    @classmethod
    def sphere_surface_sq(cls, radius):
        """
        Площадь поверхности сферы
        :param radius: радиус
        :return:
        """
        return 4 * radius ** 2 * math.pi


res = MyMath.circle_len(radius=2)
print(res)
