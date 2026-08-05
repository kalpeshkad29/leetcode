class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct=len(set(nums))
        n=len(nums)
        ans=0
        for i in range(0,n):
            my_set=set()
            for j in range(i,n):
                my_set.add(nums[j])
                if len(my_set)==distinct:
                    ans+=1
        return ans

        