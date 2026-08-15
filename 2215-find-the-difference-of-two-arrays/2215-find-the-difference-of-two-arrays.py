class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[]
        for num in nums1:
            if num in nums2:
                result.append(num)
        return [list(set(nums1)-set(result)),list(set(nums2)-set(result))]
        
        