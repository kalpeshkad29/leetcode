class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=="("or char=="[" or char=="{":
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                br=stack.pop()
                if char==")" and br=="(" or char=="]" and br=="[" or char=="}" and br=="{":
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        
        