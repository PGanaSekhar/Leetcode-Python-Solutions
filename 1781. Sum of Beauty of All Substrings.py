class Solution:
    def beautySum(self, s: str) -> int:
        r=0
        for i in range(3,len(s)+1):
            for j in range(len(s)-i+1):
                a=Counter(s[j:j+i])
                r+=max(a.values())-min(a.values())
        return r
