# Deck class
from card import suits, ranks, Card
import random


class Deck:
    def __init__(self):
        # list of all of the cards
        self.deck = []
        # create from rank and suit
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle_deck(self):
        # using random shuffle function
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)
