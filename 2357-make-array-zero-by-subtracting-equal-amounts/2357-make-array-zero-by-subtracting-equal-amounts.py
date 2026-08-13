class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        
        my_set=set()
        for i in range(0,n):
            if nums[i]!=0:
                my_set.add(nums[i])
        return len(my_set)



        