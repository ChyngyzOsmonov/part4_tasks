class Soldier:
    def __init__(self, soldat):
        self.soldat = soldat

    def desc(self):
        print('{} fire:'.format(self.soldat))

class Gun(Soldier):
    def __init__(self, name):
        self.name = name
        self.bullets = 30

    def fire(self):
        for i in range(1, self.bullets +1):
            print('tigi-tish',i)
            if i == self.bullets:
                print('You must reload')

ryan = Soldier('Ryan')
ryan.desc()
type_of_gun = Gun('AK-47')
type_of_gun.bullets = 30
type_of_gun.fire()

