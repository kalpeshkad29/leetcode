class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        n=len(s)
        count1=0
        count2=0
        max1=0
        max2=0
        for ch in s:
            if ch=="1":
                count1+=1
                count2=0
                max1=max(count1,max1)
            else:
                count2+=1
                count1=0
                max2=max(count2,max2)
        if max1>max2:
            return True
        else:
            return False

        
        