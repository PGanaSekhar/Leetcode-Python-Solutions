class Solution:
    def minSteps(self, n: int) -> int:
        c=0
        p=1
        r=0
        while p!=n:
            if n%p==0:
                c=p
                r+=1
            p+=c
            r+=1
        return r
