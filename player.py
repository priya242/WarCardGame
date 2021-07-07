
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
        try:
            return self.deck.pop(0)
        except IndexError as e:
            raise e
            # print("error message for remove()---",e)

    def __str__(self):
        return f'Player {self.name} has {len(self.deck)} cards'

    def get_length(self):
        return len(self.deck)
