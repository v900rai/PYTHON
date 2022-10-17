from math import pi
import math
class cone:
    radius=6
    height=10
    slant_height=8

    def area():
        return pi*cone.radius*cone.slant_height+pi*math.pow(cone.radius,2)
    def volume():
        return 1/3*(pi*cone.radius*cone.radius*cone.height)
    def circumference():
        return 2*pi*cone.radius
print(f'area of cone is {cone.area()}')
print(f'volume of cone is {cone.volume()}')
print(f'circumference of cone is {cone.circumference()}')