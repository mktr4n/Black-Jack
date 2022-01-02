import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True

class Card:
    
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        
    
    def __str__(self):
        return self.ranks + " of " + self.suits

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
    

    def shuffle(self):
        random.shuffle(self.deck)
        
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.ranks]

        #track aces
        if card.ranks == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        #IF TOTAL VALUE > 21 AND STILL HAVE AN ACE
        # THAN CHANGE ACE TO BE A 1 INSTEAD OF 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self):
        self.total = 100  
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How much chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break


def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter h or s only!")
            continue
        break
    

def show_some(player,dealer):

    #dealer.cards[1]
    
    #show only one of the dealer's cards
    print("\n Dealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    
    #show all (2 cards) of the player's hand/cards
    print("\n Player's hand:")
    for card in player.cards:
        print(card)

        
    
def show_all(player,dealer):

    #show all the dealer's cards
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
        
    #print("n\ Dealer's hand: ",*dealer.cards,sep='\n') **ANOTHER WAY TODO FORLOOP**
    #calculate and display value
    print(f"Value of Dealer's hand is: {dealer.value}")
    

    #show all the player's cards
    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")
        

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! PUSH')



while True:

    #OPENING STATEMENT

    print("WELCOME TO BLACKJACK")

    #CREATE & SHUFFLE THE DECK, DEAL 2 CARDS TO EACH PLAYER
    deck = Deck()
    deck.shuffle()


    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())


    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    

    #SET UP THE PLAYER'S CHIPS
    player_chips = Chips()
    

    #PROMP THE PLAYER FOR THEIR BET
    take_bet(player_chips)


    #SHOW CARDS (BUT KEEP ONE DEALER CARD HIDDEN)
    show_some(player_hand,dealer_hand)
    
    
    while playing:  #recall this variable from our hit_or_stand function


        #PROMPT FOR PLAYER TO Hit or Stand
        hit_or_stand(deck,player_hand)


        #SHOW CARDS (BUT KEEP ONE DEALER CARD HIDDEN)
        show_some(player_hand,dealer_hand)


        #IF PLAYER'S HAND EXCEEDS 21, RUN player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break
        
    #IF PLAYER'S HASN'T BUSTED, PLAY DEALER'S HAND UNTIL DEALER REACHES 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            

        #SHOW ALL CARDS
        show_all(player_hand,dealer_hand)


        #RUNS DIFFERENT WINNING SCENARIOS
        if dealer_hand.value > 21:
            dealer_bursts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    #INFORM PLAYER OF THEIR CHIPS TOTAL
    print('\n Player total chips are at: {}'.format(player_chips.total))


    #ASK TO PLAY AGAIN
    new_game = input("Would you like to play another hand? y/n ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break















