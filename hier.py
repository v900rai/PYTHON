
            
class Base:
    college = 'RKGIT'

    def college_name(self):
        return self.college

class Derived1(Base):
    pass

class Derived2(Base):
    pass

obj = Derived1()
print(obj.college_name())


obj = Derived2()
print(obj.college_name())



