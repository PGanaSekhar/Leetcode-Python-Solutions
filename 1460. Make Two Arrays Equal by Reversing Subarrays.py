class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a=Counter(target)
        b=Counter(arr)
        a=sorted(a.items())
        b=sorted(b.items())
        return a==b
