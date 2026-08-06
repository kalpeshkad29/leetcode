class Solution:
    def reverse(self,num):
        result=0
        while num>0:
            last_digit=num%10
            result=(result*10+last_digit)
            num=num//10
        return result

    def isSameAfterReversals(self, num: int) -> bool:
        if self.reverse(self.reverse(num))==num:
            return True
        return False
        
        
        