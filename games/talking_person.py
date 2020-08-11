class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking")


sumit = Person("Sumit")
sumit.talk()
