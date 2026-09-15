class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict={}
        for char in s:
            if char in my_dict:
                my_dict[char]+=1
            else:
                my_dict[char]=1
        for char in t:
            if char not in my_dict:
                return False
            else:
                my_dict[char]-=1
        for v in my_dict.values():
            if v!=0:
                return False
        return True


        