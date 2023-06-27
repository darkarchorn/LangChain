class Animal:
    id = 1
    id_class = 1
    
    def __init__(self, breed, name, color):
        self.breed = breed
        self.name = name
        self.color = color
    
    @property
    def id(self):
        id = Animal.id_class
        Animal.id_class += 1
        return id

    def __str__(self):
        return f"The animal {self.id} breed is {self.breed}, has the name of {self.name} and is {self.color} colored!"
    
    @staticmethod
    def toStringStaticMethod():
        print( "Test static method!")

    @classmethod
    def from_string(cls, s):
        list = s.split('-')
        new_list = [st.strip() for st in list]
        breed, name, color= new_list
        return cls(breed, name, color)

class Dog(Animal):
    def __init__(self, breed, name, color):
        super().__init__(breed, name, color)


class Human(Animal):
    ho = None
    ten = None
    def __init__(self, breed, name, color):
        super().__init__(breed, name, color)

    @property
    def ho_va_ten(self):
        return '{}{}'.format(self.ho, self.name)

    def ho_va_ten(self):
        ho, ten = self.name.split(' ')
        self.ho = ho
        self.ten = ten

dog = Dog("German", "Dog", "Yellow")
cat = Animal("Fluffy", "Cat", "White")
print(dog)
print(cat)

human = Human.from_string("Asian- Phan Thang - Yellow")
human.ho_va_ten()
print(human.ten)

dog.toStringStaticMethod()