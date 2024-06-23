class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        r=[]
        for i in range(len(nums)//2):
            a=min(nums)
            b=max(nums)
            nums.remove(min(nums))
            nums.remove(max(nums))
            r.append((a+b)/2)
        return min(r)
