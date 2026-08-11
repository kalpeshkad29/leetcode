class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n=len(s)
        count=0
        
        for i in range(0,n-1):
            if s[i]=="0"and s[i+1]=="1":
                count+=1
        if count==0:
            return True
        return False
                
        
        