# WarCardGame
Card Game 'War' Implementation
War Card Game

# About the Game

The objective of the game is to win all of the cards. The deck is divided evenly among the players, giving each a down stack. Each player reveals the top card of their deck—this is a "battle"—and the player with the higher card takes both of the cards played and moves them to their stack. 
If the two cards played are of equal value, then there is a "war". Both players place the next three cards face down and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. This repeats until one player's face-up card is higher than their opponent's.



# Assumptions Made

* The deck will always contain 52 cards, Ignoring Jokers in the set.
* There will be only 2 players to play the game
* Each player should get 26 cards exactly when cards are distributed among the players.
* When the cards are distributed, dealer deal the cards one at a time.
* Aces are high and Two’s of (club, heart, diamond, spade) are the lowest
* Suits are ignored - only compare the ranks.
* The values of Jack, Queen, King and Ace are 11, 12, 13, 14 respectively.
* To overcome the finite rounds scenario, I switched the order in which player's cards are added to the bottom of the winning player's deck (i.e. always opponent's  card first, then the player's card itself or vice versa)
* If a player runs out of cards during a war, then that player immediately loses and the opponent player wins the game
* The game ends when one player has won all the cards.


# Future Implementations

* Addition of more players to the game in the future. The game can be played by 2-8 players.
* Adding user Interface to make it more user friendly.



