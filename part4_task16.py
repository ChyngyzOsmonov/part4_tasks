import random
from random import randint
a_army = []
b_army = []
class Sam:
    def __init__(self, name):
        self.name = name
        self.experience = 0

    def a_arm(self):
        a = randint(0, 10)
        a_army.append(a)
        

class Tom:
    def __init__(self, name):
        self.name = name
        self.experience = 0

    def b_arm(self):
        b = randint(0, 10)
        b_army.append(b)

class Soldier(Sam, Tom):
    def exper(self):
        if a_army == b_army:
            print('Draw, both have same experience.')
        elif a_army > b_army:
            self.experience +=1
            print('Sam is winner, +1 to experience. Experience is: {}'.format(self.experience))
            print("Sam's ID is {}, and soldier with ID {} follow him.".format(id(sam),id(a_army)))
        else:
            self.experience +=1
            print('Tom is winner, +1 to experience. Experience is: {}'.format(self.experience))
            print("Tom's ID is {}, and soldier with ID {} follow him.".format(id(tom),id(b_army)))

      

sam = Sam('Sam')
tom = Tom('Tom')
sam.a_arm()
tom.b_arm()
print(a_army)
print(b_army)
sold = Soldier(tom)
sold.exper()




