class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a=2**k
        b=set()
        for i in range(len(s)-k+1):
            g=s[i:i+k]
            if g not in b:
                b.add(g)
                a-=1
            if a==0:
                return True
        return False
