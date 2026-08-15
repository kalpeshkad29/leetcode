class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=len(arr)
        arr2=sorted(arr)
        mydict={}
        r=1
        for num in arr2:
            if num not in mydict:
                mydict[num]=r
                r+=1
        result=[]
        for num in arr:
            result.append(mydict[num])
        return result
        

        
        