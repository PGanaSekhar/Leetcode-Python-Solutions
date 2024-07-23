class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a={}
        for i in set(nums):
            t=nums.count(i)
            if t not in a:
                a[t]=[i]
            else:
                a[t].append(i)
                a[t]=sorted(a[t])[::-1]
        a=dict(sorted(a.items()))
        r=[]
        for i,j in a.items():
            for k in j:
                r[:]=r+[k]*i
        return r
