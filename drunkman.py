from random import shuffle

class Card():
    suits = ['пик', 'червей', 'бубей', 'треф']
    values = [None, None, '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'валет', 'дама', 'король', 'туз']

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, second_card):
        if self.value < second_card.value:
            return True
        if self.value == second_card.value:
            if self.suit < second_card.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, second_card):
        if self.value > second_card.value:
            return True
        if self.value == second_card.value:
            if self.suit > second_card.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        card_values = self.values[self.value] + ' ' + self.suits[self.suit]
        return card_values

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self, n):
        self.wins = 0
        self.card = None
        self.name = n

class Game():
    def __init__(self):
        first_player_name = input("Имя Первого Игрока: ")
        second_player_name = input("Имя Второго Игрока: ")
        self.deck = Deck()
        self.first_player = Player(first_player_name)
        self.second_player = Player(second_player_name)

    def wins(self, w):
        winner = f"{w} забирает карты"
        print(winner)

    def draw(self, p1n, p1c, p2n, p2c):
        drawn_cards = f"{p1n} кладёт {p1c}, а {p2n} кладёт {p2c}"
        print(drawn_cards)

    def play_game(self):
        cards = self.deck.cards
        print('Начали!')
        while len(cards) >= 2:
            response = input("Введите X для выхода, любую другую букву для продолжения: ")
            if response == 'X':
                break
            first_player_card = self.deck.remove_card()
            second_player_card = self.deck.remove_card()
            first_player_name = self.first_player.name
            second_player_name = self.second_player.name
            self.draw(first_player_name, first_player_card, second_player_name, second_player_card)
            if first_player_card > second_player_card:
                self.first_player.wins += 1
                self.wins(self.first_player.name)
            else:
                self.second_player.wins += 1
                self.wins(self.second_player.name)
        win = self.winner(self.first_player, self.second_player)
        print(f"Игра Окончена! {win} победил!")

    def winner(self, p1n, p2n):
        if p1n.wins > p2n.wins:
            return p1n.name
        if p1n.wins < p2n.wins:
            return p2n.name
        return 'Ничья!'

game = Game()
game.play_game()
