class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        curr=0
        max_sum=0
        my_set=set()
        for right in range(n):
            while nums[right] in my_set:
                my_set.remove(nums[left])
                curr-=nums[left]
                left+=1

            my_set.add(nums[right])
            curr=curr+nums[right]
            max_sum=max(max_sum,curr)
        return max_sum
