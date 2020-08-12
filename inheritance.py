class Mammal:
    def walk(self):
        print("walking")


class Cat(Mammal):
    pass


class Dog(Mammal):
    def bark(self):
        print("barking")


cat = Cat()
cat.walk()

dog = Dog()
dog.walk()
dog.bark()
