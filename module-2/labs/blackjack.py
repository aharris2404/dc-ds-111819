# card
# deck
# hand

# table

# player
# dealer

# chips
# game
from itertools import product
from random import shuffle
from collections import deque

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.suit}{self.value}'

class BlackJackCard(Card):
    def score(self):
        try:
            return int(self.value)
        except ValueError as e:
            if self.value in ('J', 'Q', 'K'):
                return 10
            elif self.value == 'A':
                return 11
            else raise e

class Deck:
    def __init__(self):
        suits = ('H', 'S', 'C', 'D')
        values = ('A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        cards = list(product(suits, values))

        self.cards = deque([Card(s, v) for s, v in cards])

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, n=1):
        return (self.cards.popleft() for _ range(n))

    def return_card(self, card):
        if isinstance(card, Card):
            self.cards.append(Card)

class BlackJackHand:
    def __init__(self, cards=None):
        self.cards = deque()
        for card in cards:
            self.add_card(card)

    def get_card(self, card):
        if isinstance(card, Card):
            self.cards.append(card)

    def __str__(self):
        return ", ".(card.__str__() for card in self.cards)

    def value(self):
        val = 0
        num_aces = 0
        for card in self.cards:
            if card.value == 'A':
                num_aces += 1
            val += card.score
        if value > 21 and num_aces:
            value -= 10
