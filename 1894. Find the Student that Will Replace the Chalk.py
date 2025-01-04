class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        for i,j in enumerate(chalk):
            k-=j
            if k<0:
                return i
