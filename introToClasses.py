class MyClass:
    pass

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} barks!"
    
    def woof(self):
        return f"{self.name} says woof!"
        

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 2)
print(dog1.bark()) # Outputs: Buddy barks!

class GermanShepard(Dog):
    def guard(self):
        return f"{self.name} is guarding!"
    
gs_dog = GermanShepard("Rex", 3)
print(gs_dog.guard()) # Outputs: Rex is guarding!

dog3 = Dog("Junior", 3)
dog4 = Dog("Joseph", 3)
dog5 = Dog("Cody", 4)
dog6 = Dog("Timmy", 4)
print(dog3.woof())
print(f"The fourth dog's name is {dog4.name}.")
print(f"{dog5.name} is {dog5.age} years old.")
print(f"{dog3.name} and {dog4.name} are the same age.")
print(f"{dog3.name}, {dog4.name}, {dog5.name}, and {dog6.name} are all friends!")