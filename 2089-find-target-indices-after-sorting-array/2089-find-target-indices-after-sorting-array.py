class Solution:
    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        nums.sort()
        result=[]
        for i in range(0,n):
            if nums[i]==target:
                result.append(i)
        return result


        