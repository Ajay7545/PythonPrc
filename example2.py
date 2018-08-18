import example  as ea

ea.area(4)

#wap using fun to   add data to a list

def addlist(liss,ite):
    liss.append(ite)

listt=[]
addlist(listt,'5')
addlist(listt,'2')
addlist(listt,'4')
addlist(listt,'1')
print(listt)

#*args & **kwargs
#

def  test_value(a,b,c):
    print("it does nothing")
test_value(21,23,2)
#test_value(12)  #positional argu error
test_value(a=23,b=34,c=3)
test_value(b=2,c=1,a=45)


def multiply(x,y=2):    #polymorphism   try to give defaut argument  from right side
    print(x,y,x*y)
multiply(2,5)
multiply(10)
multiply(x=4)

def  defaultdemo(x=2,y=3,z=1):
    print(x,y,z,'=',x+y+z)
defaultdemo()
defaultdemo(5)

def pattern(char='*',size=5):
    for i in range(size):
        print(char*i)
pattern()
pattern('$',4)
pattern(char='^')

def evens(*args):
    for j in args:
        if j%2==0:
            print(j,True)
        else:
            print(j,False)
evens(2,3,5,6,7,34,23)

def leng(*args):
    s=0
    for i in args:
        s=s+1
    return s
def summ(*args):
    av=0
    for i in args:
        s=s+i
    return s
def average(*args):
    s=0
    a=len(args)
    for i in args:
        s=s+i
    print(s)
    avg=s/a
    print(avg)

average(1,4,6,9)

#kwargs
#keyword arguments
def save_info(path,**kwargs):
    file=open(path,'w')
    for key in kwargs:
        file.write(f'{key}={kwargs.get(key)}\n')
    file.close()

save_info(path='abc.txt',mobile='a device',name='something',date='22-12-72')


def addstring(*args):
    file=open('abc.txt','a')
    for i in args:
        file.write(f'{i} \n')
        print(i)
    file.close()
str='nvcgfghhhvvh'
addstring(str,'sdhsdghsjffs','sljkdvjhsdjhv')


def inputm(prompt='>>'):
    data=''
    while True:
        line=input(prompt)
        if line:
            data+=line+'\n'
        else:
            break
    return data
print(inputm())


def hello(a,b):
    c=a+b
    return c
print(hello(12,13))

def sqcube(num=2):
    sq=num**2
    cube=num**3
    return sq,cube
result=sqcube(5)
print(type(result))
s,c=sqcube(4)
print(s)
print(c)

def aboutcicircle(radius=5):
    area=3.14*radius**2
    per=2*3.14*radius
    print(area,per)
    return area,per
a,p=aboutcicircle(1)
print("the area is",a)
print("the perameter is",p)
