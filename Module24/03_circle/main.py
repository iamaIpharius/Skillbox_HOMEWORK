import math


class Circle:
    pi = math.pi

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return self.pi * (self.r ** 2)

    def perimetr(self):
        return 2*self.pi*self.r

    def grow(self, k):
        self.r = k * self.r

    def check(self, another_circle):
        x_between = abs(self.x - another_circle.x)
        y_between = abs(self.y - another_circle.y)
        rad_sum = self.r + another_circle.r

        if x_between < rad_sum and y_between < rad_sum:
            return True
        else:
            return False


dot_1 = Circle(0, 0, 3)
dot_2 = Circle(5, 4, 2)
dot_3 = Circle(4, 4, 2)

print(dot_1.check(dot_2))
print(dot_1.check(dot_3))