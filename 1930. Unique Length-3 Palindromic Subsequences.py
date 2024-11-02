class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        t=set(s)
        r=0
        for i in t:
            a=s.find(i)
            b=s.rfind(i)
            if a<b:
                r+=len(set(s[a+1:b]))
        return r
#because the middle element should be a unique element which makes it a unique palindrome
