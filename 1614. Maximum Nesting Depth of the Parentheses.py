class Solution:
    def maxDepth(self, s: str) -> int:
        r,t=0,0
        for i in s:
            if i=='(':
                t+=1
                r=max(r,t)
            elif i==')':
                t-=1
        return r
