class Person:
    name = "[name]"
    occupation = "[occupation]"

    def info(self):
        print(f"Hello my name is {self.name} and I work as {self.occupation}")


atharva = Person()

# atharva.name = "Atharva"
# atharva.occupation = "Student"

atharva.info()