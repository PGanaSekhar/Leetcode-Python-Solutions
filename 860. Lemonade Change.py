class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        req={10:[5],20:[10,5]}
        h=[]
        for i in bills:
            if i==10:
                if 5 not in h:
                    return False
                else:
                    h.remove(5)
            elif i==20:
                if h.count(10)>=1 and h.count(5)>=1:
                    h.remove(10)
                    h.remove(5)
                elif h.count(5)>=3:
                    h.remove(5)
                    h.remove(5)
                    h.remove(5)
                else:
                    return False
            h.append(i)
        return True
