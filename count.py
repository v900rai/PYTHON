class Armstrong:

    def __init__(self, num):
        self.num = num
    def count_of_digits(self):
        res =0
        if isinstance(self.num, int) is True:
            res = len(str(self.num))

        elif isinstance(self.num, str) is True:
            res =len(self.num) 
            self.num= int(self.num)

            return res
if __name__ =='__main__':
    o = Armstrong('34567834567')
    print(type(o.num))
    print(o.count_of_digits())
    print(type(o.num))
                      