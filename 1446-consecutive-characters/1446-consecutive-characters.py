class Solution:
    def maxPower(self, s: str) -> int:
        n=len(s)
        count=1
        max_count=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1
            max_count=max(count,max_count)
        return max_count


            
        