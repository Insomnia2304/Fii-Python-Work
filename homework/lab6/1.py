class Shape:
    def area(self):
        raise NotImplementedError('This method should be implemented in a derived class')
    def perimeter(self):
        raise NotImplementedError('This method should be implemented in a derived class')
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height * 1.0
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a + self.b + self.c) / 2 # semiperimeter
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5 # Heron
    def perimeter(self):
        return self.a + self.b + self.c
    
shapes = [Circle(5), Rectangle(3, 4), Triangle(3, 4, 5)]
for shape in shapes:
    print(shape.area(), shape.perimeter())
