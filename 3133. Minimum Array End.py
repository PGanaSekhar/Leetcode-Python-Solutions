class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n==1:
            return x
        t=list(bin(x)[2:])
        n-=1
        g=list(bin(n)[2:])
        for i in range(len(t)):
            if t[len(t)-i-1]=='0':
                if len(g):
                    t[len(t)-i-1]=g.pop(-1)
        t[:]=g+t
        return int(''.join(t),2)
