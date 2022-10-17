# Define a class for Checking Armstrong number

class Check :

    # Constructor
    def __init__(self,number) :
        self.num = number
        
    # define a method for checking number is Armstrong or not 
    def isArmstrong(self) :

        # copy num attribute to the temp variable
        temp = self.num
        res = 0

        # run the loop untill temp is not equal to zero
        while(temp != 0) :
            
            rem = temp % 10

            res += rem ** 3

            # integer division
            temp //= 10

        # check result equal to the num attribute or not
        if self.num == res :
            print(self.num,"is Armstrong")
        else :
            print(self.num,"is not Armstrong")


# Driver code 
if __name__ == "__main__" :
    
    # input number
    num = 6
    
    # make an object of Check class
    check_Armstrong = Check(num)
    
    # check_Armstrong object's method call
    check_Armstrong.isArmstrong()
    
    num = 127
    check_Armstrong = Check(num)
    check_Armstrong.isArmstrong()      
 #Output

 #153 is Armstrong
#127 is not Armstrong