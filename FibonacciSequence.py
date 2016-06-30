# Fibonacci Sequence
# Dave Chang
# 2016/06/30

# generator for fibonacci sequence
def fibonacciGen(number):
	a = 1
	b = 1
	for i in range(number):
		yield a
		a, b = b, a+b

# ask user to enter a number
def askNumber():
	while True:
		try:
			enterNumber = int(raw_input('Please enter a number: '))
		except:
			print 'Please enter a valid number!'
			continue
		else:
			if enterNumber > 0:
				return enterNumber
				break

# main function
if __name__ == '__main__':
	userNumber = askNumber()
	print '---Fibonacci Sequence up to %s---' %(userNumber)
	for i in fibonacciGen(userNumber):
		print i