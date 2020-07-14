import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds' ]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards =[]

for suit in suits:
    for rank in ranks:
        cards.append(f'{rank} of {suit}')

print(f'There are {len(cards)} cards in the deck')

print('Dealing ...')

hand =[]
while len(hand) < 5:
    choice = random.choice(cards)
    cards.remove(choice)
    hand.append(choice)

print(f'There are {len(cards)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)