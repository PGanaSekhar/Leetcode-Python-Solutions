class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=0
        f=0
        while r<len(nums):
            if nums[l]==nums[r]:
                    f+=1
            else:
                l=r
                f=1
            if f>2:
                nums.pop(r)
                r-=1
            r+=1
