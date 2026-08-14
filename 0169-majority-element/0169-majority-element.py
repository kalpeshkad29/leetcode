class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        mydict={}
        for num in nums:
            if num in mydict:
                mydict[num]+=1
            else:
                mydict[num]=1
        return max(mydict,key=mydict.get)
        