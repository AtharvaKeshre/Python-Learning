class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius) # I have called the costrutor of the parent class and then in the below return statement I have called the area() mrthod of the parent class
    def area(self):
        return 3.141 * super().area()

    
rec = Shape(4,5)
print(rec.area())
cir = Circle(5)
print(cir.area())