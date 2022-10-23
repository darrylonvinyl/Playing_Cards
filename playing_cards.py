from random import shuffle

"""This module contains a deck and a card class to simulate real playing 
cards."""

class Card:
    card_dict = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8: "8", 9:"9",
                    10:"10", 11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.name = self.card_dict[value]
    
    def __str__(self):
        return f"{self.name} of {self.suit}"
    

class Deck:
    suits = ["Spades","Clubs","Hearts","Diamonds"]
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for card in range(2,15):
                self.cards.append(Card(card,suit))
        shuffle(self.cards)
    
    def draw(self):
        try:
            self.cards.pop()
        except RuntimeError:
            print("No more cards remaining in the deck!")