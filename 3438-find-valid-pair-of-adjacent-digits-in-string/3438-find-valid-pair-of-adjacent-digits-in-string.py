class Solution:
    def findValidPair(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]

            if a != b and freq[a] == int(a) and freq[b] == int(b):
                return a + b

        return ""