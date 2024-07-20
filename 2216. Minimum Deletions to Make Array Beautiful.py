class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i=0
        r=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
                r+=1
            else:
                i+=2
        if len(nums)%2!=0:
            return r+1
        return r
