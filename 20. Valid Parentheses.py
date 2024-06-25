class Solution:
    def isValid(self, s: str) -> bool:
        a={'(':')','[':']','{':'}'}
        r=[]
        for i in s:
            if i in a.keys():
                r.append(i)
            else:
                if len(r)==0:
                    return False
                if i!=a[r[-1]]:
                    return False
                else:
                    r.pop(-1)
        if len(r)>0:
            return False
        return True
