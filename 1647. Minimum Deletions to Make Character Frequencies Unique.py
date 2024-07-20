class Solution:
    def minDeletions(self, s: str) -> int:
        a=Counter(s)
        r=0
        g=set()
        for i,f in a.items():
            while f>0 and f in g:
                r+=1
                f-=1
            g.add(f)
        return r
