class Solution:
    def findValidPair(self, s: str) -> str:
        n=len(s)
        my_dict={}
        for char in s:
            if char in my_dict:
                my_dict[char]+=1
            else:
                my_dict[char]=1
        for i in range(n-1):
            a=s[i]
            b=s[i+1]
            if a!=b and my_dict[a]==int(a) and my_dict[b]==int(b):
                return a+b
        return ""
            
            