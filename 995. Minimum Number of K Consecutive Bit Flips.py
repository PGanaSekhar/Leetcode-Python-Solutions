class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if k==1:
            return nums.count(0)
        r=0
        while 0 in nums and nums.index(0)<len(nums)-k+1:
            a=nums.index(0)
            for i in range(k):
                nums[a+i]= int(not nums[a+i])
            r+=1
        if nums.count(0)>=1:
            return -1
        return r
