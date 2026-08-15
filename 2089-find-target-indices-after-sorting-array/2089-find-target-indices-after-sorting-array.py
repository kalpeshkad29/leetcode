class Solution:
    def lowerBound(self,nums,target):
        n=len(nums)
        lb=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    
    def upperBound(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lb=self.lowerBound(nums,target)
        ub=self.upperBound(nums,target)
        if lb==len(nums) or nums[lb]!=target:
            return []
        return list(range(lb,ub))

        