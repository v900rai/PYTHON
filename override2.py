class parent:
    def marry(self):
     print('ram')
     print(self,'parent')
  
class child(parent):
    def marry(self):
     print('sham')
     print(self,'child')

o=child()
o.marry()
obj =parent()
obj.marry()
