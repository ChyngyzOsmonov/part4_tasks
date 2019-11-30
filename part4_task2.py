class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = 0
        self.is_flying = False

    def description(self):
        air = self.make + ' ' + self.model + ' ' + str(self.year) + ' ' + str(self.max_speed) + ' ' + str(self.odometr) + ' ' + str(self.is_flying)
        return air.title()

    def flyed(self):
        if self.odometr > 0:
            print("This airplane fly " + str(self.odometr) + " km.")
        else:
            print('Airplane stayed')
    

    def fly(self):
        if self.odometr > 0:
            self.is_flying = True
            print('Airplane is flying')
        else:
            self.odometr = 0
            self.is_flying = False
            print('Airplane is not flying')

new_air = Airplane('Pegasus', 'Airbus', 2017, 9000)
print(new_air.description())
new_air.odometr = 0
new_air.flyed()
new_air.fly()