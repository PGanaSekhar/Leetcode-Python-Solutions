class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            if nums[abs(i)-1]<0:
                pass
            else:
                nums[abs(i)-1]*=-1
        r=[]
        for i in range(len(nums)):
            if nums[i]>0:
                r.append(i+1)
        return r
        
