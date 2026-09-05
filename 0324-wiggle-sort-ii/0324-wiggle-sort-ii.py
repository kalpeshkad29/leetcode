class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n=len(nums)
        sorted_arr=sorted(nums)
        mid=(n+1)//2
        left=sorted_arr[:mid]
        right=sorted_arr[mid:]
        i=len(left)-1
        j=len(right)-1
        k=0
        while k<n:
            nums[k]=left[i]
            i-=1
            k+=1
            if k<n:
                nums[k]=right[j]
                j-=1
                k+=1

        