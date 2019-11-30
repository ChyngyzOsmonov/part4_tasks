class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
        
#принимаeт расстояние в км
    def drive(self):
        if self.odometer > 700:
            print('You do not have enough fuel ')
        else:
            print('You can drive ')
        #return self.odometer
       
        
#добавляет километры к значению одометра      
    def __subtract_fuel(self):
            #return self.odometer
         print(str(self.odometer) + 'km')
        

#отнимет потраченное количество бензина        
    def __add_distance(self):
        benz = self.odometer / 10
        benz1 = self.fuel - benz
        if benz1 < 0:
            print('You have not enough fuel, please fill the fuel')
        else:
            print('You have: ', benz1)

auto = Car('AUDI', 'A4', 2016)
auto.odometer = 750
print(auto.drive())
auto._Car__subtract_fuel()
auto._Car__add_distance()