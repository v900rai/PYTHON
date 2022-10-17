from math import pi
class shape():
    def area(self):
        pass
    def perimeter(self):
        pass
    def volume(self):
        pass
class circle(shape):

    radius=5
    
    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return pi*self.radius

class square(shape):
    side= 4
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4

class cone(shape):
    r=7
    h=9
    sh=10
    def area(self):
        return pi*self.r*self.sh.pi*self.r**2
    def volume(self):
        return 1/3*(pi*self.r*self.r*self.h)
    def perimeter(self):
        return 2*pi*self.r

class cuboid(shape):
    length =2
    width =3
    height =6

    def area(self):
        return 2*(self.length*self.width+self.width.height+self.height*self.length) 

    def perimeter(self):
        return 4*(self.length+self.width+self.height)
    def volume(self):
        return self.length*self.width*self.height

                  



obj= circle()
print(f'rea of circle={obj.area()}')
print(f'perimeter of the circle'={obj.perimeter()}\n)
