class Square:
    """
    Базовый квадрат
    """
    def __init__(self, side: int) -> None:
        """
        Инициализация
        :param side: сторона квадрата
        """
        self._side = side

    def s(self) -> int:
        """
        Нахождение площади
        :return: Площадь
        """
        return self._side ** 2

    def p(self) -> int:
        """
        Нахождение периметра
        :return: Периметр
        """
        return self._side * 4

    @property
    def side(self) -> int:
        """
        Геттер, сторона квадрата
        :return: сторона квадрата
        """
        return self._side

    @side.setter
    def side(self, new_value: int) -> None:
        """
        Сеттер, сторона квадрата
        :param new_value: сторона квадрата
        :return: None
        """
        self._side = new_value


class Triangle:
    """
    Базовый треугольник
    """
    def __init__(self, height: int, foundation: int) -> None:
        """
        Инициализация
        :param height: высота
        :param foundation: основание
        """
        self._height = height
        self._foundation = foundation

    def s(self) -> float:
        """
        Нахождение площади
        :return: площадь
        """
        return (self._height * self._foundation) / 2

    def p(self) -> int:
        """
        Нахождение периметра
        :return: периметр
        """
        return self._height * 2 + self._foundation

    @property
    def height(self) -> int:
        """
        Геттер, высота
        :return: высота
        """
        return self._height

    @height.setter
    def height(self, new_value: int) -> None:
        """
        Сеттер, высота
        :return: высота
        """
        self._height = new_value

    @property
    def foundation(self) -> int:
        """
        Геттер, основание
        :return: основание
        """
        return self._foundation

    @foundation.setter
    def foundation(self, new_value: int) -> None:
        """
        Сеттер, основание
        :return: основание
        """
        self._foundation = new_value


class Cube(Square):
    """
    Куб
    """
    def __init__(self, side: int) -> None:
        """
        Инициализация
        :param side: сторона квадрата 
        """
        super().__init__(side)
        self._cube = [Square(side) for _ in range(6)]

    def s_surface_cube(self) -> int:
        """
        Площадь поверхности куба
        :return: Площадь поверхности куба
        """
        result = 0
        for cub in self._cube:
            result += cub.s()
        return result


class Pyramid(Triangle):
    """
    Пирамида
    """
    def __init__(self, height: int, foundation: int) -> None:
        """
        Инициализация
        :param height: высота треугольника
        :param foundation: основание основание
        """
        super().__init__(height, foundation)
        self._pyramid = [Triangle(height, foundation) for _ in range(4)]

    def s_sutface_pyr(self) -> int:
        """
        Площадь поверхности пирамиды
        :return: Площадь поверхности пирамиды
        """
        result = 0
        for cub in self._pyramid:
            result += cub.s()
        return result


a = Cube(6)
print(a.s_surface_cube())

