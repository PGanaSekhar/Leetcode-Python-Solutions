class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)])==a:
                return True
        return False
