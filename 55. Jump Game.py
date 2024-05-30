class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        r=0
        for i in range(len(nums)):
            if i>r:
                break
            r=max(r,nums[i]+i)
            if r>=len(nums)-1:
                return True
        return False
