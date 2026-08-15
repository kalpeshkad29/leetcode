class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        n=len(numbers)
        for i in range(0,n):
            need=target-numbers[i]
            if need in seen:
                return [seen[need]+1,i+1]
            seen[numbers[i]]=i
        