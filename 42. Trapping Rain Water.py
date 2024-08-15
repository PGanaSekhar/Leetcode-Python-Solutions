class Solution:
    def trap(self, height: List[int]) -> int:
        l=[max(height[:i]) for i in range(1,len(height)+1)]
        r=[max(height[i:]) for i in range(len(height))]
        res=0
        print(len(height))
        for i in range(len(height)):
            res+=min(l[i],r[i])-height[i]
        return res
