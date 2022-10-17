from math import pi
class circle:
    r=None

    def area(self):
        return pi*self.r**2

obj = circle()
obj.r=10
print(obj.area()) # circle .area(obj)

o = circle()
o.r = 5
print (o.area()) #circle.area(o)