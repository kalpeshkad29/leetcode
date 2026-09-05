class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict={}
        for char in s:
            
            my_dict[char]=my_dict.get(char,0)+1
        for i in range(len(s)):
            if my_dict[s[i]]==1:
                return i
        return -1
        