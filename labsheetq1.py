list1 = []
for i in range(0,5):
	r = eval(input('enter a value into the list : '))
	list1.append(r)
#for i in range(0,5):
#	print(list1[i])
def print_big_enough(list1,n):
#	s = int(n)
	for i in range(0,len(list1)):
		if(list1[i] > n):
			print(list1[i],end=" ")
print_big_enough(list1,5)
