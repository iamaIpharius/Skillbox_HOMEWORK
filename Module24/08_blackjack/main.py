import random


class Card:
    def __init__(self, name, lear, value):
        self.value = value
        self.name = name
        self.lear = lear


class Deck:
    cards_names = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}
    lears = ['Черви', 'Бубны', 'Трефы', 'Пики']

    def __init__(self):
        self.cards = []
        for name, value in self.cards_names.items():
            for lear in self.lears:
                self.cards.append(Card(name, lear, value))


class Dealer:

    def __init__(self, Deck):
        self.score = 0
        self.cards = []
        self.playing_deck = Deck
        for _ in range(2):
            self.my_card = random.choice(self.playing_deck.cards)
            self.cards.append(self.my_card)
            self.playing_deck.cards.remove(self.my_card)
            self.score += self.my_card.value

    def opening(self):
        return self.score


class Player:

    def __init__(self, Deck):
        self.score = 0
        self.cards = []
        self.playing_deck = Deck
        for _ in range(2):
            self.my_card = random.choice(self.playing_deck.cards)
            self.cards.append(self.my_card)
            self.playing_deck.cards.remove(self.my_card)
            self.score += self.my_card.value

    def get_more(self):
        self.my_card = random.choice(self.playing_deck.cards)
        if self.score > 21 and self.my_card.value == 11:
            self.my_card.value = 1
        self.cards.append(self.my_card)
        self.playing_deck.cards.remove(self.my_card)
        self.score += self.my_card.value

    def info(self):
        print('Ваши карты:\n')
        for card in self.cards:
            print(f'{card.name} {card.lear}\n')
        print('\n Ваш счет -', self.score, '\n')

    def opening(self):
        return self.score

    def play(self, dealer):
        print('Игра началась!')
        playing = True

        while playing:
            self.info()
            print('Берем карту или останавливаемся?')
            choice = input('1 - берем, 2 - останавливаемся: ')

            if choice == '1':
                self.get_more()
                if self.opening() > 21:
                    self.info()
                    print('Вы проиграли!')
                    playing = False
            elif choice == '2':
                player_result = self.opening()
                dealer_result = dealer.opening()
                if player_result > 21:
                    print('Вы проиграли!')
                    playing = False
                elif player_result == 21:
                    print('Вы выиграли!')
                    playing = False
                elif player_result > dealer_result:
                    print(f'Ваш результат - {player_result}, результат дилера - {dealer_result}')
                    print('Вы выиграли!')
                    playing = False
                elif player_result == dealer_result:
                    print(f'Ваш результат - {player_result}, результат дилера - {dealer_result}')
                    print('Ничья!')
                    playing = False
                else:
                    print(f'Ваш результат - {player_result}, результат дилера - {dealer_result}')
                    print('Вы програли!')
                    playing = False
            else:
                print('Введена неизвестная команда')

new_deck = Deck()

new_player = Player(new_deck)
new_dealer = Dealer(new_deck)

new_player.play(new_dealer)

