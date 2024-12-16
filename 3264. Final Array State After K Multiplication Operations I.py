class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            a=min(nums)
            nums[nums.index(a)]*=multiplier
        return nums
