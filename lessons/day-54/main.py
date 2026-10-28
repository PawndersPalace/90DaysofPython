class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


pet = Dog("Pip")
print(f"{pet.name} says {pet.speak()}")
