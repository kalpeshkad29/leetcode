class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        stack=[]
        num=0
        sign="+"
        for i in range(n):
            char=s[i]
            if char.isdigit():
                num=num*10+int(char)
            if char in "+-*/" or i==n-1:
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-num)
                elif sign=="*":
                    stack.append(stack.pop()*num)
                elif sign=="/":
                    stack.append(int(stack.pop()/num))
                sign=char
                num=0
        return sum(stack)
        