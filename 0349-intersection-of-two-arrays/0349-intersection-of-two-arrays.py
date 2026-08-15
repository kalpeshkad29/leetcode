class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=set()
        for val in nums1:
            if val in nums2:
                result.add(val)
                
            
        return list(result)
        