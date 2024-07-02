class Person():
    def __init__(self, name, occupation): # This is the syntax of creating a constructor. 
        self.name = name                  # Its a function that automatically invokes and initializes the variables
        self.occupation = occupation      # Here I am initializing the variables which I have passes when I created an object of this class (See the object creation)

    def info(self):
        print(f"My name is {self.name} and I am {self.occupation}")


atharva = Person("Atharva", "Developer")

atharva.info()