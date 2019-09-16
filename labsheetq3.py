list1 = []
for i in range(0,10):
	r = eval(input('Enter the number in the list : '))
	list1.append(r)
def special_sort(list1):
	elist = []
	olist = []
	flist = []
	for i in range(0,len(list1)):
		if(list1[i] % 2 == 0):
			elist.append(list1[i])
		else:
			olist.append(list1[i])
	elist.sort()
	olist.sort()
	for i in range(0,len(elist)):
		flist.append(elist[i])
	for j in range(0,len(olist)):
		flist.append(olist[j])
	for i in range(0,len(flist)):
		print(flist[i],end = ",")
special_sort(list1)

