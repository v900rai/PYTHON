def overload(a=None,b=None):
    if a==None and b==None:
        print('no arge were passed')
    elif a !=None and b==None:
        print(f'{a=}only one args was passed')
    elif a != None and b !=None:
        print(f'{a=}and{b=} both args were passed')
    elif a == None and b !=None:
        print(f'{b=} only one args wase passed')

if __name__=='__main__':
    overload(b=2)
                        

    

    


