class Solution:
    def rotatedDigits(self, n: int) -> int:
        r=0
        for i in range(1,n+1):
            a=str(i)
            if '3' in a or '7' in a or '4' in a:
                continue
            if '2' in a or '5' in a or '6' in a or '9' in a:
                r+=1
        return r
