class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        t=nums.count(1)
        m=0
        a=0
        n=len(nums)
        l=0
        for r in range(2*n):
            if nums[r%n]:
                a+=1
            if r-l+1 > t:
                a-=nums[l%n]
                l+=1
            m=max(m,a)
        return t-m
