name = 'Ms Dhoni'
print(name)
print(id(name))
def hometown():
    global name # redeclear
    name = 'Mahi' #this statement is not reint it dect in local name space
    print( name, ' from the function ')  #mahi
    print(id(name)) #local namespace
hometown() 
print(name) #mahi global namespace 
print(id(name))  


