class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        my_set=set()
        for i in range(0,n):
            
            for j in range(i+1,n):
                the_set=set()
                for k in range(j+1,n):
                    fourth=target-(nums[i]+nums[j]+nums[k])
                    if fourth in the_set:
                        temp=[nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        my_set.add(tuple(temp))
                    the_set.add(nums[k])  
        fin_ans=[]
        for ans in my_set:
            fin_ans.append(list(ans))
        return fin_ans

        

        