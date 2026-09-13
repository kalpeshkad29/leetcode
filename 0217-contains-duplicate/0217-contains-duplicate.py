class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        my_dict={}
        for num in nums:
            if num in my_dict:
                my_dict[num]+=1
            else:
                my_dict[num]=1
        for value in my_dict.values():
            if value>1:
                return True
        
        return False
        



        