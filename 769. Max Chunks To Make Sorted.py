class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        r=0
        m=-1
        for i,j in enumerate(arr):
            m=max(m,j)
            if m==i:
                r+=1
        return r
