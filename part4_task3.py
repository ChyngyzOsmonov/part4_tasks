length = int(input('Enter distance: '))
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70


    def desc(self):
        return ('{} {} {}'.format(self.make,self.model,self.year))


#принимаeт расстояние в км
    def drive(self):
        return self.odometer
        
            
#добавляет километры к значению одометра      
    def __subtract_fuel(self):
        km = self.odometer + length
        print('Distance: {}km'.format(km))


#отнимет потраченное количество бензина        
    def __add_distance(self):
        benz = length / 10
        benz1 = self.fuel - benz
        if benz1 < 0:
            print('You have not enough fuel, please fill the fuel')
        else:
            print('You have: ', benz1)

auto = Car('AUDI', 'A4', 2016)
print(auto.desc())
auto.drive()
auto._Car__subtract_fuel()
auto._Car__add_distance()

            