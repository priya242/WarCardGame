# !/usr/bin/python3
import time
from deck import Deck
from player import Player

p1 = Player("one")
p2 = Player("two")


class Game:
    # start the game
    player1 = p1
    player2 = p2

    # create the deck
    newDeck = Deck()

    # shuffle the deck
    newDeck.shuffle_deck()

    # divide and distribute the cards to both players
    def distribute(self, all_cards):
        # total_cards = int(all_cards.length() / 2)
        for x in range(26):
            self.player1.add(all_cards.deal())
            self.player2.add(all_cards.deal())
        print("length of player1", self.player1.get_length())
        print("length of player2", self.player2.get_length())
        return self.player1, self.player2

    # method that contains the main logic of game
    def start_game(self, player1, player2):
        self.distribute(self.newDeck)
        # initializing the variables
        winner = False;
        round = 0

        # game start time
        start = time.time()

        while winner == False:
            round += 1
            print("Round ", round)
            print(player1.__str__())
            print(player2.__str__())
            if len(player1.deck) == 0:
                print("Player 2 wins!")
                winner = True

                break
            if len(player2.deck) == 0:
                print("Player 1 wins!")
                winner = True;
                break

            # start the new game
            player1_cards = [player1.remove()]
            player2_cards = [player2.remove()]

            isWar = True

            while isWar:
                if player1_cards[-1].value > player2_cards[-1].value:
                    # player1 will take all of the cards
                    player1.add(player2_cards)
                    player1.add(player1_cards)
                    isWar = False

                elif player2_cards[-1].value > player1_cards[-1].value:
                    # player2 will take all of the cards
                    player2.add(player1_cards)
                    player2.add(player2_cards)
                    isWar = False

                else:
                    # Check if players have sufficient cards to draw
                    if len(player1.deck) < 4:
                        winner = True;
                        print("----------------------------------")
                        print("Game Stop : Player 2 is the winner")
                        break

                    elif len(player2.deck) < 4:
                        winner = True;
                        print("----------------------------------")
                        print("Game Stop : Player 1 is the winner")
                        break

                    else:
                        print("WAR HAS BEGUN!")
                        # each player draw 4 cards - 3 down and 1 up
                        for num in range(4):
                            player1_cards.append(player1.remove())
                            player2_cards.append(player2.remove())

        # end time
        end = time.time()

        # total time taken
        print(f"Game took {(end - start) * 1000} ms")


# start the card war game

def main():
    game = Game()
    game.start_game(p1, p2)


if __name__ == '__main__':
    main()
