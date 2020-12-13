from tkinter import *
from Card import *
from Deck import *
from Player import *



def main():
    deck = Deck()
    dealer = Hand()
    caden = Player("Caden", "200")


    deck.shuffle()


    # Place your bets
    player.newHand(5)


    # First card for all the player's hands
    hand = player.getHands()[0]
    card = deck.getTopCard();
    card.flip()
    hand.addCard(card)

    # Dealer's down card
    card = deck.deal();
    dealer.addCard(deck.deal())

    # Second card for all the player's hands
    for player in players:
        for hand in player.getHands():
            card = deck.deal();
            card.flip()
            hand.addCard(card)

    # Dealer's up card
    card = deck.deal();
    card.flip()
    dealer.addCard(deck.deal())



    print(player)
    print("\n\n")
    print(dealer)



    if dealer.getTotal() == 21:
        player.lose()
        dealer.win()

    for player in players:
        for hand in player.getHands():
            player.win(hand.bet * 1.5)
            if hand.getTotal() == 21:
                del hand




main()
