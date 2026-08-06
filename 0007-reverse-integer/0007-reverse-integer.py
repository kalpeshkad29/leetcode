class Solution:
    def reverse(self, x: int) -> int:
        
        result=0
        negative=x<0
        num=abs(x)

        while num:
            
                
            last_digit=num%10
            result=(result*10)+last_digit
            num=num//10
        if  negative:
            result= result*(-1)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
        