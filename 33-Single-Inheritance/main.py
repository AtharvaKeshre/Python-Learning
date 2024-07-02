class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Meow")

d = Dog("Dog", "Snow")
d.make_sound()

d = Cat("Cat", "Simba")
d.make_sound()

a=Animal("Doggie","Doggu")
a.make_sound()