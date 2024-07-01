class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s)%2!=0 and '*' not in s:
            return False
        a,b=0,0
        for i in s:
            if i=='(':
                a+=1
                b+=1
            elif i=='*':
                b+=1
                a=max(a-1,0)
            else:
                b-=1
                a=max(a-1,0)
            if b<0:
                return False
        return a==0
