from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        super().__init__()

    @abstractmethod
    def produce_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            raise Exception("Invalid input!")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age == "" or int(age) < 0:
            raise Exception("Invalid input!")
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender == "":
            raise Exception("Invalid input!")
        self.__gender = gender


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Meow meow"


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Ribbit"


class Kitten(Cat):
    def __init__(self, name, age, gender=None):
        Cat.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age, gender=None):
        Cat.__init__(self, name, age, gender)

    def produce_sound(self):
        return "MEOW"


def classify(cls, name, age, gender):
    if cls == "Dog":
        obj = Dog(name, age, gender)
    elif cls == "Cat":
        obj = Cat(name, age, gender)
    elif cls == "Frog":
        obj = Frog(name, age, gender)
    elif cls == "Kitten":
        gender = "Female"
        obj = Kitten(name, age, gender)
    elif cls == "Tomcat":
        gender = "Male"
        obj = Tomcat(name, age, gender)
    return obj


animals = []

while True:
    cls = input()
    if cls == "Beast!":
        break
    try:
        data = input().split()
        name = data[0]
        age = data[1]
        gender = data[2]
        obj = classify(cls, name, age, gender)
        animals.append(obj)
    except Exception as exception:
        print(exception)
        continue

for animal in animals:
    print(animal.__class__.__name__)
    print(f"{animal.name} {animal.age} {animal.gender}")
    print(animal.produce_sound())