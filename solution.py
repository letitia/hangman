from harness import *

numGuesses = 5
guesses = []

while numGuesses > 0:
	print wordProgress(guesses)
	print 'You have ' + str(numGuesses) + ' guesses remaining.'
	guess = getLetter()

#	if guess == False:
#		continue

#	if guess in guesses:
#		print "You already guessed " + guess + "!"
#		continue
	
	guesses.append(guess)

	if letterIsInWord(guess):
		print 'Congrats! "' + guess + '" is in the secret word.'
		if wordIsCompleted(guesses):
			print 'You win!!'
			revealSecretWord()
			break
	else:
		print 'Sorry, "' + guess + '" is not in the secret word.'
		numGuesses = numGuesses - 1

if numGuesses == 0:
	print 'Game over.  You lost.'
	revealSecretWord()
		
