class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a=list(set(word))
        return sum(1 if i.upper() in a and i.lower() in a else 0 for i in a)//2
