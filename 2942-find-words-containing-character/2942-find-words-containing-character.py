class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n=len(words)
        result=[]
        for i in range(0,n):
            for char in words[i]:
                if char==x:
                    result.append(i)
                    break
        return result


        