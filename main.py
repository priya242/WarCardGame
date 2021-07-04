#!/usr/bin/python3
# Libraries

from random import shuffle
import random

# intializing the variables
player1 = []
player2 = []
deck = [1, 2, 2, 4, 5, 6, 7, 8, 9, 10]

winner = False;
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

round = 1

# start the new game
player1_cards = []
player1_cards.append(player1.pop(0))
player2_cards = []
player2_cards.append(player2.pop(0))

while winner == False:
    print("Round ", round)

    if player1_cards[-1] > player2_cards[-1]:
        # player1 will take all of the cards
        # player1.append(player2[0])
        # player2.pop(0)
        # player1.append(player1[0])
        # player1.pop(0)
        if len(player1_cards) == 1:
            player1.append(player1_cards[-1])
            player1.append(player2_cards[-1])
        elif len(player1_cards) > 1:
            for num in range(len(player1_cards)):
                player1.append(player1_cards[-1])
                player1.append(player2_cards[-1])

    elif player2_cards[-1] > player1_cards[-1]:
        # player2 will take all of the cards
        if len(player2_cards) == 1:
            player2.append(player1_cards[-1])
            player2.append(player2_cards[-1])
        elif len(player2_cards) > 1:
            for num in range(len(player2_cards)):
                player2.append(player1_cards[-1])
                player2.append(player2_cards[-1])
    else:
        print("war")
        if len(player1) < 3:
            print("Player 2 is the winner")
        elif len(player2) < 3:
             print("Player 1 is the winner")
        else:
            # compare the third card
            for num in range(3):
                player1_cards.append(player1.pop(0))
                player2_cards.append(player2.pop(0))


    round += 1;

    if len(player1) == 0:
        print("Player 2 wins!")
        winner = True;

    if len(player2) == 0:
        print("Player 1 wins!")
        winner = True;

