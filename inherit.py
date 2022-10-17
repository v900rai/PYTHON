class Base:
    college = 'RKGIT'

    def college_name(self):
        return self.college

class Derived(Base):
    pass

obj = Derived()
print(obj.college_name())
