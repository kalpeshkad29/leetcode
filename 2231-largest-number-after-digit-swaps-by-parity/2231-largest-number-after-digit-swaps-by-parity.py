class Solution:
    def largestInteger(self, num: int) -> int:
        num1=str(num) 
        even=[]
        odd=[]
        
        for digit in num1:
            if int(digit)%2==0:
                even.append(digit)
            else:
                odd.append(digit)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        e=0
        o=0
        result=""
    
        for digit in num1:
            if int(digit)%2==0:
                result+=even[e]
                e+=1
            else:
                result+=odd[o]
                o+=1
        return int(result)
        
