class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l=len(part)
        while part in s:
            a=s.index(part)
            s=s[:a]+s[a+l:]
        return s
