#from Inheritance import SuperHuman
#from classesdemo import Mobile
#from classesdemo import Mobile2
#from classesdemo import Calculator

from AllContent.Calc import Calculator
from AllContent.College import SuperHuman

class Department:
    def __init__(self,name,age,mno,addr,dob):
        self.name=name
        self.age=age
        self.mno=mno
        self.addr=addr
        self.dob=dob

    def printval(self):
        print(f'Hi {self.name} You are {self.age}\n Contact Detail: {self.mno}\n You are From {self.addr}\n'
              f'your date of birth is {self.dob}')

class Student(Department):
    def __init__(self,branch,year,eno):
        self.branch=branch
        self.year=year
        self.eno=eno

class Faculty(Department):
    def __init__(self,dep,teacherid,salary):
        self.dep=dep
        self.teacherid=teacherid
        self.salary=salary

    def work(self,workh):
        self.workh=workh
        print(f'You are  Working {self.workh} in a day')

if __name__=='__main__':
    print("Value of pie",22/7)
    s1=Student('cse',1,16103177)
    print(s1.branch,s1.year,s1.eno)
    Student.name='Ajay'
    s1.age=21
    Student.dob='4/7/1996'
    Student.mno=9169151514
    Student.addr='Lucknow'
    s1.printval()
    #Student.printval() error
    fac1=Faculty('CSE',1514,45000)
    fac1.name='PK Tiwari'
    fac1.age=41
    fac1.mno=9161251417
    fac1.dob='1/1/1950'
    fac1.addr='Pakistan'
    fac1.printval()
    fac1.work(12)
    c1=Calculator()
    c1.add(2,2,6,4)
    c1.mul(2,5,2)
    sup1=SuperHuman('ajay','king',25,'m',['stamin','speed'])
    sup1.secretidentity()