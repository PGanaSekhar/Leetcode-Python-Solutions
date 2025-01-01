class Solution:
    def maxScore(self, s: str) -> int:
        r=0
        for i in range(len(s)-1):
            r=max(r,s[:i+1].count('0')+s[i+1:].count('1'))
        return r
