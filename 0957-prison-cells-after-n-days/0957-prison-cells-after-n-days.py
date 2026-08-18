class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen={}
        while n>0:
            state=tuple(cells)
            if state in seen:
                cycle_length=seen[state]-n
                n %=cycle_length
            seen[state]=n
            if n>0:
                n-=1
                next_day=[0]*8
                for i in range(1,7):
                    if cells[i-1]==cells[i+1]:
                        next_day[i]=1
                cells=next_day
        return cells


        
      

        