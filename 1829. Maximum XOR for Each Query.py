class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        x=0
        for i in nums:
            x^=i
        m=(1<<maximumBit)-1
        r=[]
        for i in reversed(nums):
            r.append(x^m)
            x=x^i
        return r
