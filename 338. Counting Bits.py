class Solution:
    def countBits(self, n: int) -> List[int]:
        r=[]
        for i in range(n+1):
            r.append(bin(i).count('1'))
        return r
