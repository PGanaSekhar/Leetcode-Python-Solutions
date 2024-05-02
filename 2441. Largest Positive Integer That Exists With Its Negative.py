class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        return max([i if -i in nums and i in nums else -1 for i in nums])
