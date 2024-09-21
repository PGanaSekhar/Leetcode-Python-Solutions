class Solution:
    def shortestPalindrome(self, s: str) -> str:
        a=s[::-1]
        for i in reversed(range(len(s)+1)):
            if s[:i]==s[:i][::-1]:
                if i==1:
                    return s[1:][::-1]+s
                return s[i:][::-1]+s
        return ""
