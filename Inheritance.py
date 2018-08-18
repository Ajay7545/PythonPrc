# inheritance and operater overloding

class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def eat(self,food):
        print(f'{self.name}\n Eats{food}')
    def sleeps(self,duration):
        print(f'{self.name} Sleep {duration} Hours')
    def work(self,duration):
        print(f'{self.name} Works {duration} hours')

class SuperHuman(Human):
    def __init__(self,name,hero_name,age,gender,power=[]):
        super().__init__(name,age,gender)
        self.power=power
        self.hero=hero_name

    def rescue(self,enemy,noofpeople=0):
        print(f'{self.hero} saves {noofpeople} from {enemy}')
    def secretidentity(self):
        print(f'{self.hero} is actually {self.name}')

if __name__== '__main__':
    superman=SuperHuman('Clark kert' , 'superman',29,'male',power=['Super Strength','fly','eat like bhukkad'])
    superman.work(12)
    superman.rescue('mokambo',12)
    superman.sleeps(15)
    superman.eat('dhoop')
    superman.secretidentity()
    human=Human('Ajay',21,'Male')
    human.eat(' Shahi Paneer')
    human.sleeps(12)
