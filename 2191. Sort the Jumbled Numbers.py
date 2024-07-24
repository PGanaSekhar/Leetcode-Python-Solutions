class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        a={}
        for i in nums:
            g=""
            for j in str(i):
                g+=str(mapping[int(j)])
            h=int(g)
            if h not in a:
                a[h]=[i]
            else:
                a[h].append(i)
        a=dict(sorted(a.items()))
        return [i for j in a.values() for i in j]
