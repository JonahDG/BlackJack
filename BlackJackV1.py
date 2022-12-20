import random

# Create Deck
values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suits=['Hearts','Diamonds','Clubs','Spades']
deck=[(value,suit) for value in values for suit in suits]
# Shuffle Deck
random.shuffle(deck)

# Hands
playerHand=[deck.pop(),deck.pop()]
print(f'Your Hand is {playerHand}')

playerVal=0
for card in playerHand:
	if card[0] in ['J','Q','K']:
		playerVal+=10
	elif card[0]=='A':
		playerVal+=11
	else:
		playerVal+=card[0]
print(f'Your Current Value is {playerVal}')

dealerHand=[deck.pop(),deck.pop()]
print(f'The Dealer is showing {dealerHand[0]}')

move=input('Would you like to hit or stay? ')
while move.lower()=='hit':
	playerHand.append(deck.pop())
	