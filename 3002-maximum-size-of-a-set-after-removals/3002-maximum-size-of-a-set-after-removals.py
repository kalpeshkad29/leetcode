class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)

        s1 = set(nums1)
        s2 = set(nums2)

        only1 = len(s1 - s2)
        only2 = len(s2 - s1)
        common = len(s1 & s2)

        take1 = min(only1, n // 2)
        take2 = min(only2, n // 2)

        remaining = n - take1 - take2

        return take1 + take2 + min(common, remaining)
        
        
        