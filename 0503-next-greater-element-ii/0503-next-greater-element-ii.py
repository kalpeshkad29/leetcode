class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        new_list=nums+nums
        n=len(new_list)
        stack=[]
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=new_list[i]:
                stack.pop()
            if len(stack)!=0:
                ans[i]=stack[-1]
            
            stack.append(new_list[i])
        return ans[0:n//2]
        