class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        a=[-1]
        r=0
        for i in range(len(nums)):
            if nums[i]%2:
                a.append(i)
            if len(a)>k+1:
                a.pop(0)
            if len(a)==k+1:
                r+=a[1]-a[0]
        return r
