
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def add(self, cards):
        # check if player has any cards or not
        if type(cards) == type([]):
            self.deck.extend(cards)
        else:
            self.deck.append(cards)

    def remove(self):
        return self.deck.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.deck)} cards'
