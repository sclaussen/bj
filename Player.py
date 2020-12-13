from Hand import *



class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = float(bankroll)
        self.hands = []

    def newHand(self, bet):
        hand = Hand()
        hand.setBet(bet)
        self.hands.append(hand)

    def getHands(self):
        return self.hands

    def win(self, winnings):
        self.bankroll += winnings

    def __str__(self):
        s = self.name + "\n\n"
        for hand in self.hands:
            s += hand.__str__() + "\n"
        s += "\nBankroll: " + str(self.bankroll)
        return s
