class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        r=0
        s=0
        for i in range(1,min(n+1,maxSum)):
            if i not in banned and s+i<=maxSum:
                r+=1
                s+=i
        return r
