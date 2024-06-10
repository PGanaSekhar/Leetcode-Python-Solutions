class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a=sorted(heights)
        r=0
        for i in range(len(a)):
            if a[i]!=heights[i]:
                r+=1
        return r
