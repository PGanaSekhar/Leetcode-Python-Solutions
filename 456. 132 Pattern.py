class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        second_num = -math.inf
        stck = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_num:
                return True
            while stck and stck[-1] < nums[i]:
                second_num = stck.pop()
            stck.append(nums[i])
        return False
        
