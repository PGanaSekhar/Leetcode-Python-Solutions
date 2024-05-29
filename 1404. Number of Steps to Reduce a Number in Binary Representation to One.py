class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        r=0
        while a>=2:
            print(a)
            if a%2==0:
                a//=2
            else:
                a+=1
            r+=1
        return r
