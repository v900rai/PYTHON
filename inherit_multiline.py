class Base:
    college = 'RKGIT'

    def college_name(self):
        return self.college

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

obj = Derived2()
print(obj.college_name())
