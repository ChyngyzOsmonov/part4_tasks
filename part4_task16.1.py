import random
from random import randint
a_army = []
b_army = []

def mixed_army():
        n = randint(0,35)
        for i in range(0, n):
            if i % 2 == 0:
                a_army.append(i)
            elif i % 2 != 0:
                b_army.append(i)
mixed_army()

class Sam:
    def __init__(self, name):
        self.name = name
        self.experience = 0
        

class Tom:
    def __init__(self, name):
        self.name = name
        self.experience = 0


class Soldier(Sam, Tom):
    
    def exper(self):
        if len(a_army) == len(b_army):
            print('Draw, both have same experience.')
        elif len(a_army) > len(b_army):
            self.experience +=1
            print('Sam is winner, +1 to experience. Experience is: {}'.format(self.experience))
            print("Sam's ID is {}, and soldier with ID {} follow him.".format(id(sam),id(a_army)))
        else:
            self.experience +=1
            print('Tom is winner, +1 to experience. Experience is: {}'.format(self.experience))
            print("Tom's ID is {}, and soldier with ID {} follow him.".format(id(tom),id(b_army)))

        
sam = Sam('Sam')
tom = Tom('Tom')
print("Amount Sam's soldiers: ",len(a_army))
print("Amount Tom's soldiers: ",len(b_army))
sold = Soldier(sam)
sold.exper()





