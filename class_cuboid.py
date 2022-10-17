class cuboid:
    length=2
    width=3
    height=5

    def area():
        return 2*(cuboid.length*cuboid.width+cuboid.width*cuboid.height+cuboid.height*cuboid.length)

    def perimeter():
        return 4*(cuboid.length+cuboid.width+cuboid.height)

    def volume():
        return cuboid.length*cuboid.width*cuboid.height
 
print(f'area of cuboid is {cuboid.area()}')
print(f'perimeter of cuboid is {cuboid.perimeter()}')
print(f'volume of cuboid is {cuboid.volume()}')