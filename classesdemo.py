5# class classname:
#    def functionname(self,[parameter]...): self is predefine keyword in clss
#        code
#    variable=value
#   to allian all ctrl + alt+ L

class Mobile:
    model = 'abc'
    ram = '2GB'
    rom = '32GB'
    price = 1300

    def info(self):
        print(f'model={self.model}')
        print(f'ram={self.ram}')
        print(f'rom={self.rom}')
        print(f'only Rs.={self.price}')

    def updateprice(self, price):
        self.price = price


class Student:
    rollno = 10
    name = 'ajay'
    age = 21

    def updatename(self, name):
        self.name = name

    def info(self):
        print(f'Name={self.name}\nAge={self.age}\nRollno={self.rollno}')


class Mobile2:

    def __init__(self, price, model, configuration, company):
        self.price = price
        self.model = model
        self.configuration = configuration
        self.company = company

    def info2(self):
        print(f'Price={self.price},Model={self.model},Configuration={self.configuration},Company={self.company}')


class Calculator:
    def add(self, *args):
        s = 0
        for i in args:
            s = s + i
        print("Add", s)

    def sub(self, a, b):
        c = a - b
        print("Subtract:", c)

    def div(self, a, b):
        c = a / b
        print("Divide:", c)

    def mul(self, *args):
        mu = 1
        for i in args:
            mu = mu * i
        print("Multiply result :", mu)


if __name__ == '__main__':
    m1 = Mobile()
    m1.info()
    m1.updateprice(5000)
    m1.info()
    print(type(m1))
    s1 = Student()
    s1.info()
    m2 = Mobile2(7000, 'note 8', '16GB RAM 8GB ROM', 'Samsung')
    # m2.configuration='asf'
    m2.model = "samsung galaxy s8"
    m2.info2()
    cal = Calculator()
    cal.add(4, 5, 6, 7)
    cal.sub(8, 4)
    cal.mul(5, 6, 4, 1)
    cal.div(9, 2)
