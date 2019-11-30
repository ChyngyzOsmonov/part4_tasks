class Student:
    def __init__(self, name, last_name, age, lesson):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.lesson = lesson

    def desc(self):
        print('"{} {}", {}, "{}"'.format(self.name,self.last_name,self.age,self.lesson))

Steve = Student('Steven', 'Schultz', 23, 'English')
Johnny = Student('Jonathan', 'Rosenberg', 24, 'Biology')
Penny = Student('Penelope', 'Meramveliotakis', 21, 'Physics')
Penny.desc()
Johnny.desc()
Steve.desc()