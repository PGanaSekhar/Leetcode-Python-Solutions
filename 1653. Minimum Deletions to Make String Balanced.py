class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=[]
        r=0
        for i in s:
            if i=='a':
                if len(a):
                    r+=1
                    a.pop(-1)
            else:
                a.append(i)
        return r
