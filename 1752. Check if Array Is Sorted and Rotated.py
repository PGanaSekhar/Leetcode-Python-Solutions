class Solution:
    def check(self, nums: List[int]) -> bool:
        b=0
        for i in range(nums.count(min(nums))):
            a=nums[b:].index(min(nums))+b
            if sorted(nums)==nums[a:]+nums[:a]:
                return True
            b=a+1
        return False
