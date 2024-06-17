class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        b=list(string.ascii_lowercase)
        b.extend(string.digits)
        a=""
        for i in s:
            if i in b:
                a+=i
        return a==a[::-1]
