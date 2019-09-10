import random
import math

totalGuessCount = 0
guessCounter = 0

def guess_work():
	numbOfGuessesTaken = 0
	global totalGuessCount
	global guessCounter
	guess = 0
	allowedGuesses = 0
	n = int(input("Please enter a number n:"))
	randomNumb = random.randint(1,n)

	#Calculating the allowed guesses
	allowedGuesses = int(1 + math.log(n,2))

	#Let's start guessing
	print('Please start guessing')
	while numbOfGuessesTaken < allowedGuesses-1:
		guess = int(input())
		numbOfGuessesTaken = numbOfGuessesTaken + 1

		if guess < randomNumb:
			print('l')

		if guess > randomNumb:
			print('h')

		if guess == randomNumb:
			break


	guessCounter = guessCounter + 1
	if guess != randomNumb:
		numbOfGuessesTaken = numbOfGuessesTaken + 1
	totalGuessCount = totalGuessCount + numbOfGuessesTaken
	averageGuesses = totalGuessCount / float(guessCounter)

	if guess == randomNumb and numbOfGuessesTaken < allowedGuesses:
		print('It took me '+str(numbOfGuessesTaken)+' guesses')
		print('I averaged '+str(averageGuesses)+' guesses per game for '+str(guessCounter)+' game(s)')

	if guess != randomNumb:
		print('Your number is '+str(randomNumb))
		print('It took me '+str(numbOfGuessesTaken)+' guesses')
		print('I averaged '+str(averageGuesses)+' guesses per game for '+str(guessCounter)+' game(s)')

	reply = input('Play again (y/n)?')

	if reply[0] == 'y':
		guess_work()
	
	if reply[0] == 'n':
		return False



guess_work()
