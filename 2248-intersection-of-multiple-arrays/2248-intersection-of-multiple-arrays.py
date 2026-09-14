class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        my_dict={}
        for arr in nums:
            for num in arr:
                if num in my_dict:
                    my_dict[num]+=1
                else:
                    my_dict[num]=1
        result=[]
        for k,v in my_dict.items():
            if v==n:
                result.append(k)
        return sorted(result)

        