import unittest
import main
from card import Card
from player import Player
from deck import Deck


# unit test class
class TestWarCardGame(unittest.TestCase):
    test_cards = Deck()

    # check if the deck has a list of cards or not
    def test_checkNulls(self):
        self.assertFalse(self.test_cards.length() == 0)

    # cards should be equal to 52
    def test_cardCount(self):
        self.assertFalse(self.test_cards.length() != 52)

    # test if each player is getting equal cards
    def test_distribute(self):
        p1, p2 = main.distribute(self.test_cards)
        self.assertEqual(p1.get_length(), p2.get_length())

    # check exception is raised when there are no cards left in the list
    def test_no_card(self):
        player = Player("test")
        player.add(self.test_cards)
        total_cards = self.test_cards.length()

        for _ in range(total_cards + 1):
            player.remove()
        with self.assertRaises(IndexError):
            player.remove()

    # test cards equality
    def test_equality(self):
        card1 = Card('Spade', 'Ace')
        card2 = Card('Heart', 'Ace')
        card3 = Card('Clubs', 'Ten')
        card4 = Card('Diamonds', 'Five')
        card5 = Card('Spade', 'King')
        card6 = Card('Heart', 'Queen')
        self.assertEqual(card1.value, card2.value)
        self.assertNotEqual(card1.value, card3.value)
        self.assertNotEqual(card2.value, card3.value)
        self.assertNotEqual(card3.value, card4.value)
        self.assertNotEqual(card4.value, card5.value)
        self.assertNotEqual(card5.value, card6.value)

    # test start game with a deck of two cards
    def test_start_game(self):
        player1 = Player("1")
        player2 = Player("2")
        player1.add(Card('Spades', 'Ace'))
        player2.add(Card('Spades', 'King'))
        main.start_game(player1, player2)
        # winner should have total cards and loser left with 0 cards
        self.assertEqual(player1.get_length(), 2)
        self.assertEqual(player2.get_length(), 0)


if __name__ == '__main__':
    unittest.main()
