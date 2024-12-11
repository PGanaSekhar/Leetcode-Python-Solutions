class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def counting(val):
            r=0
            j=len(nums)-1
            for i in range(len(nums)):
                while i<j and nums[i]+nums[j]>val:
                    j-=1
                r+=max(0,j-i)
            return r

        nums.sort()
        return counting(upper)-counting(lower-1)
