name = 'Ms Dhoni'
print(name)
print(id(name))
def hometown():
     # global name # redeclear
    name = 'Mahi' #this statement is not reint it dect in local name space
    print( name, ' from the function ')  #mahi
    print(id(name)) #local namespace
    def sis():
        nonlocal name #enclosed scope
        name = 'bhai'
        print('inner most ', name)
        print(id(name)) # local name space 
    sis()    
hometown() 
print(name) #mahi global namespace 
print(id(name))  


