from math import pi

class shape():
    def area(self):
        pass

    def peri(self):
        pass

class circle( shape):
    radious = 5
    def area(self):

        return 2*pi*self.radious**2

    def peri(self):
        return 2*pi*self.radious

class square(shape):
    side =4

    def area(self):
        return self.side**2

class cone(shape):
    radious=5
    height=6
    slant_height=10

    def area(self):
        return pi*self.radious*self.height+pi*self.radious**2

    def peri(self):
        return 2*pi*self.radious
obj = circle()
print(f'area of the circle{obj.area()}')
print(f'perimeter of the circle{obj.peri()}')

obj1=square()
print=(f'area of the square{obj1.area()}')