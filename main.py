# !/usr/bin/python3
# Libraries

from deck import Deck

# intializing the variables
player1 = []
player2 = []
winner = False;
round = 0
# create the deck
newDeck = Deck()

# shuffle the deck
newDeck.shuffle_deck()

# divide and distribute the cards to each players
# distribution of cards
for x in range(26):
    player1.append(newDeck.deal())
    player2.append(newDeck.deal())

# print(player1)
# print(player2)

while winner == False:
    round += 1
    print("Round ", round)
    # print(player1)
    # print(player2)
    if len(player1) == 0:
        print("Player 2 wins!")
        winner = True
        break
    if len(player2) == 0:
        print("Player 1 wins!")
        winner = True;
        break

    # start the new game
    player1_cards = [player1.pop(0)]
    player2_cards = [player2.pop(0)]

    isWar = True

    while isWar:
        if player1_cards[-1].value > player2_cards[-1].value:
            # player1 will take all of the cards
            for num in range(len(player1_cards)):
                player1.append(player2_cards[num])
                player1.append(player1_cards[num])
            isWar = False

        elif player2_cards[-1].value > player1_cards[-1].value:
            # player2 will take all of the cards
            for num in range(len(player2_cards)):
                player2.append(player1_cards[num])
                player2.append(player2_cards[num])
            isWar = False

        else:
            # Check if players have sufficient cards to draw
            if len(player1) < 4:
                winner = True;
                print("Player 2 is the winner")
                break

            elif len(player2) < 4:
                winner = True;
                print("Player 1 is the winner")
                break

            else:
                print("WAR HAS BEGUN!")
                # each player draw 4 cards - 3 down and 1 up
                for num in range(4):
                    player1_cards.append(player1.pop(0))
                    player2_cards.append(player2.pop(0))




