import numpy as np
def main():
    values=np.array([2,3,4,5,6,7,8,9,10,'J','Q','K','A'])
    suits=np.array(['Hearts','Diamonds','Clubs','Spades'])
    deck=np.array([[value,suit] for value in values for suit in suits])
    np.random.shuffle(deck)
    playerHand,dealerHand,deck=dealOpeningHands(deck)
    playerVal=calcHand(playerHand,'y')
    dealerVal=calcHand(dealerHand,'n')
    print(f'In your hand you have a(n) %s of %s and a %s of %s.'%(playerHand[0][0],playerHand[0][1],playerHand[1][0],playerHand[1][1]))
    playerVal=calcHand(playerHand,'y')
    if playerVal==21:
        print('BLACKJACK!')
        playAgain=input('Would you Like to play again (y/n)?' )
        if playAgain=='y':
            main()
        else:
            quit()
    print(f'The dealer is showing a %s of %s'%(dealerHand[0][0],dealerHand[0][1]))
    if dealerHand[0][0] in [10,'J','Q','K','A'] and dealerVal==21:
        print('The Dealer has Blackjack')
        playAgain=input('Would you like to play again (y/n)? ')
        if playAgain=='y':
            main()
        else:
            quit()
    elif dealerHand[0][0]=='A' and dealerVal!=21:
        print('The Dealer\'s hidden card is not a Face or 10 Card and does not have Blackjack.')
    elif dealerHand[0][0] in [10,'J','Q','K'] and dealerVal !=21:
        print('The Dealer\'s hidden card is not an Ace and does not have Blackjack')
    while True:
        action=input('Would you like to hit or stay? ')
        if action.lower()=='hit':
            playerHand,deck=hit(playerHand,deck)
            print(f'Your hand now also has a(n) %s of %s.'%(playerHand[-1][0],playerHand[-1][1]))
            playerVal=calcHand(playerHand,'y')
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
    dealerVal=calcHand(dealerHand,'y')
    while True:
        dealerVal=calcHand(dealerHand,'y')
        print(dealerHand)
        print(dealerVal)
        if dealerVal==17 and 'A' in dealerHand:
            dealerHand,deck=hit(dealerHand,deck)
            
        elif dealerVal>=17:
            break
        else:
            dealerHand,deck=hit(dealerHand,deck)
    print('----------------------------------')
    print(f'Player Value: {playerVal}')
    print(f'Dealer Value: {dealerVal}')
    if dealerVal>21:
        print('Dealer Busts, Player WIns!')
    elif dealerVal > playerVal:
        print('Dealer Wins!')
    elif dealerVal==playerVal:
        print('Player Pushes')
    else:
        print('Player Wins')
    playAgain=input('Would you like to play again (y/n)? ')
    if playAgain=='y':
        main()
    else:
        quit()
    
def dealOpeningHands(playDeck):
    playerHand=np.array([playDeck[0],playDeck[2]])
    dealerHand=np.array([playDeck[1],playDeck[3]])
    updateDeck=np.delete(playDeck,[0,1,2,3],axis=0)
    return playerHand,dealerHand,updateDeck

def calcHand(hand,Print):
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
    if numAces==0 and Print=='y':
        print(f'This has a value of {handVal}')
    for i in range(numAces):
        if handVal>21 and Print=='y':
            handVal-=10
            print(f'This has a value of {handVal}')
        elif Print=='y':
            print(f'This has a value of soft {handVal}')
    return handVal

def hit(hand,playDeck):
    print(hand)
    return np.append(hand,np.array([playDeck[0]]),axis=0),np.delete(playDeck,[0],axis=0)


main()