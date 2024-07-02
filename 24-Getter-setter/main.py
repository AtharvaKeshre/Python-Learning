class Person():
    def __init__(self,age = 0):
        self._age = age
        print("welcome its the constructor")

    @property
    def age(self):
        print("Getter")
        return self._age
    
    @age.setter
    def age(self,age):
        print("Setter")
        self._age = age

ak = Person()
ak.age = 25
print(ak.age)