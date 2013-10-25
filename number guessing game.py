from random import randrange
totalrange=100
print "Please think of a number between 0 and %s" %totalrange
rng = randrange(totalrange+1)
guess = False
minrange=0
maxrange=totalrange
print "is your secret number %s ?" %rng
while guess == False:
	ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	if ans == "l":
		minrange = rng+1
		rng = randrange(minrange, maxrange)
		print "is your number %s" %rng
	elif ans == "h":
		maxrange = rng
		rng = randrange(minrange,maxrange)
		print "is your number %s" %rng
	elif ans == "c":
		guess=True
		break
	else:
		print "Sorry, I did not understand your input."
print "Game over. Your secret number was: %s" %rng