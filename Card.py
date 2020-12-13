class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.visibility = False

    def flip(self):
        self.visibility = True

    def __str__(self):
        value2 = self.value
        if self.value == "J":
            value2 = "J"
        elif self.value == "Q":
            value2 = "Q"
        elif self.value == "K":
            value2 = "K"
        elif self.value == "A":
            value2 = "A"

        suit2 = self.suit
        if self.suit == "S":
            suit2 = "Spades"
        elif self.suit == "C":
            suit2 = "Clubs"
        elif self.suit == "D":
            suit2 = "Diamonds"
        elif self.suit == "H":
            suit2 = "Hearts"

        return str(value2) + " of " + suit2
