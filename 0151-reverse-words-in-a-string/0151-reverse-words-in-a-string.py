class Solution:
    def reverseWords(self, s: str) -> str:
        result=" "
        words=s.split()
        words.reverse()
        return result.join(words)
