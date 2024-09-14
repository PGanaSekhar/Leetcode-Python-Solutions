class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = r = c = 0
        for i in nums:
            if m < i:
                m = i
                r = c = 0
            if m == i:
                c += 1
            else:
                c = 0
            r = max(r, c)
        return r
