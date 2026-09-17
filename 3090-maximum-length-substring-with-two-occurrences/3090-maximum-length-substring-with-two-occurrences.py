class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        max_len=0
        my_dict={}
        for right in range(n):
            if s[right] in my_dict:
                my_dict[s[right]]+=1
            else:
                my_dict[s[right]]=1
            while my_dict[s[right]]>2:
                my_dict[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
        