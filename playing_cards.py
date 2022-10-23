from random import shuffle

"""This module contains a deck and a card class to simulate real playing 
cards."""

class Card:
    """ Class for creating a playing card.

    Args:
        value (int): The number of the playing card, from 2-14, with 11 - 14
        being Jack, Queen, King, and Ace respectively.
        suit (str): The suit of the card, consisting of a string that is
        either Spades, Clubs, Diamonds or Hearts.

    Returns:
        Creates a card object.
    """
    card_dict = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8: "8", 9:"9",
                    10:"10", 11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.name = self.card_dict[value]
    
    def __str__(self):
        return f"{self.name} of {self.suit}"
    

class Deck:
    """ Class for creating a deck of playing cards. Cards consist of the Card
    class.

    Method:
        draw: Draws a card from the deck, unless the deck is empty.

    Side effects:
        Creates deck object with the option to draw cards until it's empty.
    """
    suits = ["Spades","Clubs","Hearts","Diamonds"]
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for card in range(2,15):
                self.cards.append(Card(card,suit))
        shuffle(self.cards)
    
    def draw(self):
        try:
            drawn_card = self.cards.pop()
            return drawn_card
        except RuntimeError:
            print("No more cards remaining in the deck!")