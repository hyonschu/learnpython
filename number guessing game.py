from random import randrange
def guessme():
        totalrange=101
        blah = totalrange-1
        print "Please think of a number between 0 and %s" %blah
        rng = randrange(totalrange+1)
        guess = False
        minrange=0
        maxrange=totalrange
        guesses = 1
        print "is your secret number %s ?" %rng
        while guess == False:
                ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
                if ans == "l":
                        minrange = rng+1
                        rng = randrange(minrange, maxrange)
                        print "is your number %s" %rng
                        guesses += 1
                elif ans == "h":
                        maxrange = rng
                        rng = randrange(minrange,maxrange)
                        print "is your number %s" %rng
                        guesses += 1
                elif ans == "c":
                        guess=True
                        break
                else:
                        print "Sorry, I did not understand your input."
        print "\nGame over. Your secret number was: %s \n\nIt took %s number of guesses" % (rng, guesses)
