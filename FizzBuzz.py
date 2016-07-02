# Fibonacci Sequence
# Dave Chang
# 2016/07/02
# Print 1 to 100
# Multiples of 3, print "Fizz"
# Multiples of 5, print "Buzz"
# Multiples of 3 & 5, print "FizzBuzz"

def fizzBuzz():
	for i in range(1,101):
		if i%3 == 0 and i%5 == 0:
			print 'FizzBuzz'
		elif i%3 == 0:
			print 'Fizz'
		elif i%5 == 0:
			print 'Buzz'
		else:
			print i

if __name__ == '__main__':
	fizzBuzz()