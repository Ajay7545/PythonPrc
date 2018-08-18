def display():
    print("hello world  ")
#display()

def area(r):
    a=3.14*r**2
    print(f"cirle area:{a}")

#area(5)
#for i in range(3):
 #   area(i)

def pattern(sy,si):
    for i   in  range(si):
        print(sy*i)
#pattern('*',8)
#pattern('$',5)

#wapto replace all consonent with o usinga fun

def look(str):
    vo={'a','e','i','o','u','A','E','I','O','U'}
    for i in str:
        if i not in vo:
            str=str.replace(i,'o')
    print(str)
tr=input("enter string:")
look(tr)

def sonentwitho(word):
    vowels={'a','e','i','o','u'}
    for char in word:
        if char not in vowels:
            word=word.replace(char,'o')
    print(word)
sonentwitho("AsdfsaidsOUT")
