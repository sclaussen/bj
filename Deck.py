import random
from Card import *



class Deck:

    def __init__(self):
        self.initialize()

    def shuffle(self):
        self.initialize()
        shuffledCards = []
        for _ in range(52):
            card = random.choice(self.cards)
            self.cards.remove(card)
            shuffledCards.append(card)
        self.cards = shuffledCards

    def getTopCard(self):
        return self.cards.pop(0)

    def initialize(self):
        self.cards = []
        for suit in [ "H", "D", "S", "C" ]:
            for value in [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        s = ""
        for card in self.cards:
            s2 = card.__str__()
            s = s + "\n" + s2
        return s
