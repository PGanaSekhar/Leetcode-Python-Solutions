class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if (max(nums)*(max(nums)+1))//2==sum(nums):
            return max(nums)+1
        nums=sorted(list(set(nums)))
        for i in range(len(nums)):
            if nums[i]>0:
                nums=nums[i:]
                break
        print(nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return i+2
