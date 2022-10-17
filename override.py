class parent:
    def marry(self):
     print('ram')
  
class child(parent):
    def marry(self):
     print('sham')

o=child()
o.marry()
o=parent()
o.marry()
