class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s=[0]
        r=0
        t=sum(nums)
        for i in nums:
            s.append(s[-1]+i)
        s.pop(0)
        for i in range(len(s)-1):
            if s[i]>=(s[-1]-s[i]):
                r+=1
        return r
