# Bubble sort
# Dave Chang
# 2016/07/05
'''
Algorithm
1. iterate through the whole array
2. comapre two elements next to each other, swap the element if list[i] > list[i+1]
'''

# swap aList[i] & aList[i+1]
def swapElements(aList, i):
	aList.insert(i, aList.pop(i+1))
	return aList
	
# bubble sort
def bubbleSort(aList):
	i = 0
	while i < len(aList)-1:
		j = 0
		swapping = False
		while j < len(aList)-1:
			if aList[j] > aList[j+1]:
				swapElements(aList,j)
				#print 'Swapping elements!'
				#print aList
				swapping = True
			j += 1
			
		i += 1
		#print swapping
		if swapping == False:
			return aList
			break

# ask user to input a list
def askList():
	while True:
		try:
			user_input = map(int,raw_input('Please enter a list of numbers (ex: 1,8,7...): ').split(','))
		except:
			print 'Please enter a valid input!'
			continue
		else:
			return user_input
			break

# main function
if __name__ == '__main__':
	aList = askList()
	print 'Bubble sort the list: ', aList
	print 'Sorted result:', bubbleSort(aList)