class Base:
    Two_wheel = 'Hero'


    def Two_wheel_name(self):
        return self.Two_wheel

class Derived(Base):
    pass

obj = Derived()
print(obj.Two_wheel_name())
