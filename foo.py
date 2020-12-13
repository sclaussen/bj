cards = []
for suit in [ "H", "D", "S", "C" ]:
    for value in [ "2", "3" ]:
        cards.append(suit + value)

print(cards)
card = cards.pop(0)
print(card)
print(cards)
