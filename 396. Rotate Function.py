class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        r=c=sum(i*j for i,j in enumerate(nums))
        a=sum(nums)
        l=len(nums)
        while nums:
            c+=a-nums.pop()*l
            r=max(c,r)
        return r
