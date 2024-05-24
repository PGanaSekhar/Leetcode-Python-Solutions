class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        a=[]
        for i in nums:
            if i!=0:
                a.append(i)
        for i in range(len(a)):
            nums[i]=a[i]
        for i in range(len(nums)-len(a)):
            nums[len(a)+i]=0
