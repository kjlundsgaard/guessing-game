# importing random module
from random import randint

#greet player
#get player name
name = raw_input("Hey! What's your name? ")

#print name in prompt
print "Hey %s, I'm thinking of a number between 1 and 100." % (name)

#choose random number beteen 1 and 100

def guessing_game():

    number = randint(1, 100)
    # print number

    # get guess from player
    guess = None

    # making a list of guesses
    guess_list = []
    # score_list = []
    # while True:
    while guess != number: 
        
        
        # get guess
        while True:
            guess = raw_input("Take a guess: ")
            try: 
                guess = int(guess)
                break
            except:
                print "That's not a number, dummy! Try harder"
        
        if guess < 1 or guess > 100:
            print "That number is not between 1 and 100! Try again"
        # if guess is in guess_list, print "you've already guessed that number"
        elif guess in guess_list:
            print "you've already guessed that number!"    
        
        #
        else: 
            guess_list = guess_list.append(guess)
            # if guess is incorrect:
        if guess < number:
            print "Your guess is too low! Try again."

        elif guess > number:
            print "Your guess is too high! Try again."
        # if guess is correct:
        else: 
            break


    # congratulate player
    guesses = len(guess_list)
    # score_list = score_list.append(guesses)
    # low_score = 
    print "Congratulations! The number was %d and you guessed it in %d tries" % (number, guesses)
    print "Would you like to play again?"
    play_again = raw_input("type 'y' if yes or 'n' if no: ").lower()
    if play_again == 'y':
        guessing_game()
    else:
        print "Thanks for playing, go enjoy real life."

guessing_game()

