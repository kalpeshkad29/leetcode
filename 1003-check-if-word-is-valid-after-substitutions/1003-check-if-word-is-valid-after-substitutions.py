class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            stack.append(char)
            if stack[-3:]==['a','b','c']:
                stack.pop()
                stack.pop()
                stack.pop()
        if len(stack)==0:
            return True
        return False

        
       