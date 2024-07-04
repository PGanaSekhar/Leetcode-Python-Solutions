class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if len(nums)<5:
        #     return 0
        # nums=list(set(nums))
        # a=len(nums)-4
        # return nums[a]-nums[0]
        nums.sort()
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))
