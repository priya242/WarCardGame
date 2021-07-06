# Card class consists of suit, rank  and value of card
suits = {'Diamonds', 'Clubs', 'Spades', 'Hearts'}
# increasing order
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
# dictionary to map ranks to values
values = {'Two': 2,
          'Three': 3,
          'Four': 4,
          'Five': 5,
          'Six': 6,
          'Seven': 7,
          'Eight': 8,
          'Nine': 9,
          'Ten': 10,
          'Jack': 11,
          'Queen': 12,
          'King': 13,
          'Ace': 14}


class Card:

    # constructor
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# print(Card('Spades', 'Ace'))
# print(Card('Spades', 'Ten'))
# print(Card('Hearts', 'Ten'))
