class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        n=len(hours)
        count=0
        for num in hours:
            if num>=target:
                count+=1
        return count
        