# Collatz conjecture
# Dave Chang
# 2016/07/02
'''
Start with a number n > 1
Find the number of steps it takes to reach 1 using the following process: 
If n is even, do n/2 
If n is odd, do 3n+1
'''

# count steps to reach 1 by collatz conjecture
def countSteps(number):
	count = 0
	while number > 1:
		if number%2 == 0:
			number = number/2
		else:
			number = 3*number + 1
		count += 1
	return count

# ask user to input a positive number
def askNumber():
	while True:
		try:
			number = int(raw_input('Please enter a positive numbr: '))
		except:
			print 'Please enter a valid numnber!'
			continue
		else:
			if number > 0:
				return number
				break

# main function
if __name__ == '__main__':
	number = askNumber()
	steps = countSteps(number)
	print '---Collatz conjecture---'
	print 'Total number of steps for %s to reach 1 is: %s' %(number, steps)