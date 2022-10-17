class armstrong():
    def _init_(self,num):
        self.num=num
        
    def arm(self):
        temp=self.num
        count=0
        while temp>0:
            count+=1
            temp//=10
        sum=0
        temp=self.num
        while temp>0:
            rem=temp%10
            sum+=pow(rem,count)
            temp//=10
        
        return sum==self.num
obj=armstrong(153)
print(obj.arm())
ob=armstrong(127)
print(ob.arm())