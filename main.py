# !/usr/bin/python3
# Libraries

from random import shuffle
import random

# intializing the variables
player1 = []
player2 = []
winner = False;
round = 0
deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
        10, 10, 10]

# using random shuffle function
random.shuffle(deck)

# divide the deck into half
half = (len(deck) / 2)
half = int(half)

# distribution of cards
for x in range(0, half):
    player1.append(deck[x])
print(player1)

for x in range(half, len(deck)):
    player2.append(deck[x])
print(player2)

# test case -1
# player1 = [6, 5, 2, 4, 1, 4, 8, 5, 2, 5]
# player2 = [2, 2, 6, 4, 5, 4, 9, 5, 7, 10]

while winner == False:
    round += 1
    print("Round ", round)
    print(player1)
    print(player2)
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
        if player1_cards[-1] > player2_cards[-1]:
            # player1 will take all of the cards
            for num in range(len(player1_cards)):
                player1.append(player2_cards[num])
                player1.append(player1_cards[num])
            isWar = False

        elif player2_cards[-1] > player1_cards[-1]:
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

            # print(player1)
            # print(player2)
