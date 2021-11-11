import random 

def coinFlips(flips, coins):
	oneCount = 0 #head count
	zeroCount = 0 #tails count
	options = [0,1]
	for coin in range(coins):
		for times in range(flips):
			result = random.choice(options)
			if result == 1:
				oneCount += 1
			else:
				zeroCount += 1
	print('Heads = ' + str(oneCount))
	print('Tails = ' + str(zeroCount))
	if oneCount > zeroCount:
		return 'Heads Won!'
	elif zeroCount > oneCount:
		return 'Tails Won!'
	else:
		return 'Tie!'



if __name__ == '__main__':
	coins = int(input("How many coins: "))
	flips = int(input("How many flips: "))
	results = coinFlips(flips, coins)
	print(results)