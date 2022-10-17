class parent:
    def marry(self):
        pass
     
  
class child(parent):
    def marry(self):
     print('sham')
     print(self,'child')

o=child()
o.marry()
