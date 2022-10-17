
            
class Base1:
    college = 'RKGIT'

    def college_name(self):
        return self.college

class Base2():
    col = 'SVIT'

    def college_name(self):
        return self.col



class Derived2(Base1, Base2):
    pass

obj = Derived2()
print(obj.college_name())








