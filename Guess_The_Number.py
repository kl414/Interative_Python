# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



# initialize global variables used in your code
import random, simplegui

secret_number = 0
guess_left = 0
mode = 1


# helper function to start and restart the game
def new_game():
    global secret_number, guess_left, mode
    if mode == 1:
        guess_left = 7
        secret_number = random.randrange(0, 100)
        print "New game with range 0 - 100:\n"
    else:
        guess_left = 10
        secret_number = random.randrange(0, 1000)
        print "New game with range 0 - 1000:\n"
        


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global mode 
    mode = 1
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global mode 
    mode = 0
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_left
    guess_left -= 1
    player_guess = int(guess)
    print "User guess:" , player_guess
    
    if player_guess == secret_number:
        print "You win!\nA new game will be started!\n"
        new_game()
    elif guess_left == 0:
        print "You Lose!\nA new game will be started!\n"
        new_game()
    elif player_guess > secret_number:
        print "Try guess a lower number."
        print "Remaining guesses:" , guess_left
        print
    elif player_guess < secret_number:
        print "Try guess a higher number."
        print "Remaining guesses:" , guess_left 
        print

    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 200)


# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_input("Guess", input_guess, 100)


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
