class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        a=Counter(s1)
        b=Counter(s2)
        g=set(s1).symmetric_difference(set(s2))
        for i in list(g):
            if a[i]>1 or b[i]>1:
                g.remove(i)
        return g
