import random


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


class Life:
    __karma_constant = 500
    __list_of_sins = [
        KillError,
        DrunkError,
        CarCrashError,
        GluttonyError,
        DepressionError
    ]

    def __init__(self):
        self.__current_karma = 0

    def get_karma(self):
        return self.__current_karma

    def one_day(self):
        self.__current_karma += random.randint(1, 7)
        chance_of_sin = random.randint(1, 10)
        if chance_of_sin == 1:
            sin = random.choice(self.__list_of_sins)
            with open('karma.log', 'a', encoding='utf-8') as log:
                log.write(str(sin))
                log.write('\n')


living = True
my_life = Life()
while living:
    my_life.one_day()
    my_karma = my_life.get_karma()
    if my_karma >= 500:
        print(f'Ваша карма {my_karma}, Вы просветились!')
        living = False
