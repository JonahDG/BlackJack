import numpy as np
def main():
    values=np.array([2,3,4,5,6,7,8,9,10,'J','Q','K','A'])
    suits=np.array(['Hearts','Diamonds','Clubs','Spades'])
    deck=np.array([[value,suit] for value in values for suit in suits])
    np.random.shuffle(deck)
    playerHand,dealerHand,deck=dealOpeningHands(deck)
    playerVal=calcHand(playerHand)
    dealerVal=calcHand(dealerHand)
    print(f'In your hand you have a(n) %s of %s and a %s of %s.'%(playerHand[0][0],playerHand[0][1],playerHand[1][0],playerHand[1][1]))
    if playerVal==21:
        print('BLACKJACK!')
        playAgain=input('Would you Like to play again (y/n)?' )
        if playAgain=='y':
            main()
        else:
            quit()
    else:
        if 'A' in playerHand:
            print(f'This has a value of soft {playerVal}')
        else:
             print(f'This has a value of {playerVal}.')
    print(f'The dealer is showing a %s of %s'%(dealerHand[0][0],dealerHand[0][1]))
    if dealerHand[0][0]=='A' and dealerVal==21:
        print('The Dealer has Blackjack')
        playAgain=input('Would you like to play again (y/n)? ')
        if playAgain=='y':
            main()
        else:
            quit()
    elif dealerHand[0][0]=='A' and dealerVal!=21:
        print('The Dealer\'s hidden card is not a Face or 10 Card and does not have Blackjack.')
    while True:
        action=input('Would you like to hit or stay? ')
        if action.lower()=='hit':
            playerHand,deck=hit(playerHand,deck)
            print(f'Your hand now also has a(n) %s of %s.'%(playerHand[-1][0],playerHand[-1][1]))
            playerVal=calcHand(playerHand)
            if 'A' in playerHand:
                print(f'This has a value of soft {playerVal}')
            else:
                print(f'This has a value of {playerVal}.')
            if playerVal>21:
                print('YOU BUST!')
                playAgain=input('Would you like to play again (y/n)? ')
                if playAgain=='y':
                    main()
                else:
                    quit()
        else:
            break
    print('The Dealer must hit a soft 17 or lower!')
    print(f'The Dealer\'s full opening hand is a(n) %s of %s and a(n) %s of %s.'%(dealerHand[0][0],dealerHand[0][1],dealerHand[1][0],dealerHand[1][1]))
    print('This has a value of')
    
def dealOpeningHands(playDeck):
    playerHand=np.array([playDeck[0],playDeck[2]])
    dealerHand=np.array([playDeck[1],playDeck[3]])
    updateDeck=np.delete(playDeck,[0,1,2,3],axis=0)
    return playerHand,dealerHand,updateDeck

def calcHand(hand):
    handVal=0
    numAces=0
    for card in hand:
        if card[0] in ['J','Q','K']:
            handVal+=10
        elif card[0]=='A':
            handVal+=11
            numAces+=1
        else:
            handVal+=int(card[0])
    for i in range(numAces):
        if handVal>21:
            handVal-=10
    return handVal

def hit(hand,playDeck):
    return np.append(hand,np.array([playDeck[0]]),axis=0),np.delete(playDeck,0,axis=0)


main()