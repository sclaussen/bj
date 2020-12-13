class Hand:
    def __init__(self):
        self.cards = []
        self.bet = 0
        self.soft = False
        self.total = 0
        self.maxTotal = 0

    def setBet(self, bet):
        self.bet = bet

    def addCard(self, card):
        self.cards.append(card)
        self.evaluateHand()

    def getSoft(self):
        return self.soft

    def getTotal(self):
        return self.total

    def getMaxTotal(self):
        return self.maxTotal

    def evaluateHand(self):
        self.soft = False
        self.total = 0
        self.maxTotal = 0

        for card in self.cards:
            if card.value == "J" or card.value == "Q" or card.value == "K":
                self.total += 10
                self.maxTotal += 10
            elif card.value == "A":
                self.total += 1
                self.maxTotal += 11
                self.soft = True
            else:
                self.total += int(card.value)
                self.maxTotal += int(card.value)

        if self.soft:
            if self.maxTotal > 21:
                self.soft = False
                self.maxTotal = 0

    def __str__(self):
        s = ""
        for card in self.cards:
            cardString = card.__str__()
            s += cardString + "\n"
        if self.soft:
            s += "Totals: " + str(self.total) + "/" + str(self.maxTotal)
        else:
            s += "Total: " + str(self.total)
        return s
