class Solution:
    def __init__(self):
        self.l = 0
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stk = []
        subsets = []
        self.l = len(nums)
        self.get_subsets(stk, 0, nums, subsets)

        return subsets
    def get_subsets(self,stk,start_idx,nums,subsets):
        subsets.append(list(stk))
        for i in range(start_idx,self.l):
            stk.append(nums[i])
            self.get_subsets(stk,i+1,nums,subsets)
            stk.pop()
        