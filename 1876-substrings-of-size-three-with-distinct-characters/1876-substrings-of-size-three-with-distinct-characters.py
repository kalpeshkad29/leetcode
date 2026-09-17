class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(n-2):
            temp=s[i:i+3]
            if len(set(temp))==3:
                count+=1
        return count

        