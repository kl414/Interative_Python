# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object
        self.value = 0

    def __str__(self):
        # return a string representation of a hand
        toReturn = ""	
        for card in self.cards:
            toReturn += str(card) + " "
        return toReturn
        
    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, 
        #then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        ace = 0
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = 1
        if ace == 1 and value + 10 <= 21:
            value += 10
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]
            
    def draw_dealer(self, canvas, pos):
        global in_play
        if in_play:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            pos[0] += CARD_BACK_SIZE[0]
            self.cards[1].draw(canvas, pos)
        else:
            self.draw(canvas, pos)
            
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        if len(self.deck) > 0:
            return self.deck.pop()
        
    
    def __str__(self):
        # return a string representing the deck
        toReturn = ""	
        for card in self.deck:
            toReturn += str(card) + " "
        return toReturn


#define event handlers for buttons
def deal():
    global outcome, in_play
    global deck, player, dealer, score
    # your code goes here
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    if in_play:
        outcome = "Player lose this round!"
        score -= 1
    else:
        in_play = True
        outcome = "Hit or Stand?"

def hit():
    # replace with your code below
    global deck, player, score, in_play, outcome
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
    else:
        return
    
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "You have busted! New deal?"
        in_play = False
        score -= 1
       
def stand():
    # replace with your code below
    global in_play, dealer, player, deck, score, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
    else:
        return
    # assign a message to outcome, update in_play and score
    if dealer.get_value() > 21:
        outcome = "Dealer busted! You win!"
        score += 1
    else:
        if dealer.get_value() >= player.get_value():
            outcome = "Dealer win! New deal?"
            score -= 1
        else:
            outcome = "You win! New deal?"
            score += 1
    in_play = False
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player, dealer, outcome, in_play, score
    canvas.draw_text("Blackjack", [200, 50], 50, "Purple")
    
    canvas.draw_text("Player:", [30, 130], 30, "Black")
    player.draw(canvas, [150,100])
    
    canvas.draw_text("Score: " + str(score), [30, 250], 30, "Black")
    canvas.draw_text(outcome, [200, 300], 20, "Orange")
    
    canvas.draw_text("Dealer:", [30, 430], 30, "Black")
    dealer.draw_dealer(canvas, [150, 400])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
