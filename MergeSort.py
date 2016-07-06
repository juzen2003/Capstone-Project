# Merge sort
# Dave Chang
# 2016/07/05
'''
Algorithm
1. return the list if it has only one element
2. divide the list recursively into two halves until it can no longer be divided (one element only)
3. merge the smaller lists into new list in sorted order
'''

# merge list
def mergeList(listA, listB, sortedList):
	while len(listA) > 0 and len(listB) > 0:
		if listA[0] > listB[0]:
			sortedList.append(listB[0])
			listB.remove(listB[0])
		else:
			sortedList.append(listA[0])
			listA.remove(listA[0])
	
	while len(listA) > 0:
		sortedList.append(listA[0])
		listA.remove(listA[0])
	
	while len(listB) > 0:
		sortedList.append(listB[0])
		listB.remove(listB[0])
	
	return sortedList

# merge sort
def mergeSort(aList):
	sortedList = []
	# step 1
	if len(aList) <= 1:
		return aList
	
	# step 2
	listL = aList[:len(aList)/2]
	listR = aList[len(aList)/2:]
	#print 'listL: ', listL
	listL = mergeSort(listL)
	#print 'listR: ', listR
	listR = mergeSort(listR)
	
	# step 3
	#print 'sorted list: ', mergeList(listL, listR, sortedList)
	return mergeList(listL, listR, sortedList)

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
	print 'Merge sort the list: ', aList
	print 'Sorted result:', mergeSort(aList)

		
	