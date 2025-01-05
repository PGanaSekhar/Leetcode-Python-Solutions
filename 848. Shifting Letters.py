class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        t=sum(shifts)
        r=""
        for i in range(len(s)):
            r+=chr((((ord(s[i])-97)+(t)%26)%26)+97)
            t-=shifts[i]
        return r
