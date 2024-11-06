class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        a=sorted(nums)
        if nums==a:
            return True
        m={}
        for i in nums:
            m[i]=bin(i)[2:].count('1')
        while len(nums)>1:
            a=m[min(nums)]
            for i in range(nums.index(min(nums))+1):
                if m[nums[i]]!=a:
                    return False
            nums.remove(min(nums))
        return True
