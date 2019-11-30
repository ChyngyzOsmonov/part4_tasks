class Home:
    def __init__(self, type_, bed, wardrobe, table):
        self.type_ = type_
        self.bed = bed
        self.wardrobe = wardrobe
        self.table = table

    def desc(self):
        print('Home type: {}, in the home: {}, {}, {}'.format(self.type_,self.bed,self.wardrobe,self.table))

class Furnature(Home):
    def __init__(self, bed, wardrobe, table):
        self.bed = 4
        self.wardrobe = 2
        self.table = 1.5
        self.area = 0

    def house_area(self, Home):
        print('Total area of home without furnature: ',self.area)

    def get_area(self):
        final = self.area - (self.bed + self.wardrobe + self.table)
        print('Final total area: ', final)

house = Home('flat', 'bed', 'wardrobe', 'table')
house.desc()
total_area = Furnature(4,2,1.5)
total_area.area = 55
total_area.house_area(Home)
total_area.get_area()

        

    
