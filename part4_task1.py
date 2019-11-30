class Students:
    def __init__(self, name, lastname, department, year_of_entrance):
        Students.name = name
        Students.lastname = lastname
        Students.department = department
        Students.year_of_entrance = year_of_entrance
vasya = Students('Вася', 'Иванов', 'Программирование',2017)
print(vasya.name + ' ' + vasya.lastname + ' поступил в ' + str(vasya.year_of_entrance) + ' году на факультет ' + vasya.department)