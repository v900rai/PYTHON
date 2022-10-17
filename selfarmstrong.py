# wap to find out , if a given number is  armstrong number is not 

class Armstrong():
    # initliziation number
    def __init__(self,num):
        self.num = num
        self.is_armstrong=False
    def is_armstrong_num(self):
        if self.armstrong_op(self.num)== self.num:
           self.is_armstrong=True
            # performing armstrong op 
    def armstrong_op(self,num):
        power=self.number_of_digits(num)
        res=0
        while num>0:
            last_digit=num%10
            res=sum((res,pow(last_digit,power)))
            num=self.remove_last_digit(num)
        return res
    def number_of_digits(self,num):
        count=0
        while num>0:
            count+= 1
            num=self.remove_last_digit(num)
        return count
    def remove_last_digit(self,num):
        return num//10
    def __repr__(self):
        self.is_armstrong_num()
        if self.is_armstrong is True:
            return f'{self.num} is an armstrong number'
        return f'{self.num} is not an armstrong number'
if __name__=='__main__':

        print('this code checks if a given  number is armstrong or not')
        num=int(input('enter a number......>')) 
        obj=Armstrong(num)
        print(obj)


