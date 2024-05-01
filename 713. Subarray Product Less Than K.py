class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        a=0
        if prod(nums)<k:
            return (len(nums)*(len(nums)+1))//2
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if prod(nums[i:j])<k:
                    a+=1
                else:
                    break
        return a
