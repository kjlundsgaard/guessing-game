# importing random module
from random import randint

#greet player
#get player name
name = raw_input("Hey! What's your name? ")

#print name in prompt
print "Hey %s, I'm thinking of a number between 1 and 100." % (name)

#choose random number beteen 1 and 100

number = str(randint(1, 100))
# print number

# get guess from player
guess = None

# while True:
while guess != number: 
    # get guess
    guess = raw_input("Take a guess: ")
    if guess != int(1,100)
    print "Guess an integer between 1 and 100."
    
    # if guess is incorrect:
    elif guess < number:

        # give hint
        print "Your guess is too low! Try again."
    elif guess > number:
        print "Your guess is too high! Try again."
    # else:
    else: break
        # congratulate player
print "Congratulations! The number was %s." % (number)