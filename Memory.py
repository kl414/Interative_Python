# implementation of card game - Memory

import simplegui
import random

deck = []
exposed = []
state = 0
turns = 0
card = []
# helper function to initialize globals
def new_game():
    global deck, state, turns, exposed
    deck = range(8)
    temp = range(8)
    deck.extend(temp)
    random.shuffle(deck)
    
    state = 0
    turns = 0
    
    exposed = []
    for i in range(16):
        exposed.append(0)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global card, state, turns
    idx = pos[0] // 50
    if exposed[idx] == 1:
        return
    if state == 0:
        exposed[idx] = 1
        state = 1
        card = [deck[idx], idx]
        turns += 1
    elif state == 1:
        exposed[idx] = 1
        if deck[idx] == card[0]:
            state = 0
            card = []
        else:
            card.append(idx)
            state = 2
    else:
        state = 1
        exposed[card[1]] = 0
        exposed[card[2]] = 0
        exposed[idx] = 1
        card = [deck[idx], idx]
        turns += 1
                    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, turns
    card_pos = [15, 60]
    rec_pos = [[0, 0], [50, 0], [50, 100], [0, 100]]
    for card in deck:
        canvas.draw_text(str(card), card_pos, 40, "Grey")
        card_pos[0] += 50
    for i in range(16):
        if exposed[i] == 0:
            canvas.draw_polygon(rec_pos, 1, "Black", "Green")
        for i in range(4):
            rec_pos[i][0] += 50
            
    label.set_text("Turns =" + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
