class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=Counter(arr1)
        r=[]
        print(a)
        for i in arr2:
            r.extend([i]*a[i])
            a.pop(i)
        for i in sorted(a.keys()):
            r.extend([i]*a[i])
        return r
