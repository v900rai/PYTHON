from math import pi
class circle:
    def __init__ (self,r):
        print('from init')
        self.r=r

    def area(self):
        return pi*self.r**2

obj = circle(10)

print(obj.area()) # circle .area(obj)

o = circle(5)

print (o.area()) #circle.area(o)