class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1)>len(arr2):
            arr1,arr2=arr2,arr1
        s=set()
        for i in arr1:
            while i and i not in s:
                s.add(i)
                i=i//10
        r=0
        for i in arr2:
            while i and i not in s:
                i=i//10
            if i!=0:
                r=max(r,len(str(i)))
        return r
