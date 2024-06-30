class Solution:
    def myAtoi(self, s: str) -> int:
        m=2**31
        a=""
        t=list(string.digits)
        b=['+','-']
        f=0
        for i in s:
            if i==" " and f==0:
                pass
            elif i in t:
                a+=i
                f+=1
            else:
                if f!=0 or i not in b:
                    break
                else:
                    a+=i
                    f+=1    
        print(a)           
        if a=="":
            return 0
        if len(a)==1 and a[0] not in t:
            return 0
        g=int(a)
        if g>=m-1:
            return m-1
        elif g<=(-m):
            return -m
        else:
            return g
