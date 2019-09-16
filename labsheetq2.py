list1 = []
for i in range(0,5):
	r = eval(input('enter a value into the list : '))
	list1.append(r)
def count_evens(list1):
	summ = 0
	count = 0
	for i in range(0,len(list1)):
		if(list1[i] % 2 == 0):
			count+=1
			summ = summ+list1[i]
	print("count of even = ",count)
	print("sum of even = ",summ)
count_evens(list1)
