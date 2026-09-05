class Solution:
    def repeatedCharacter(self, s: str) -> str:
        my_set=set()
        for char in s:
            if char in my_set:
                return char
        
            my_set.add(char)