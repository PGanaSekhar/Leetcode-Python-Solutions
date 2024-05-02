class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        r=0
        a=list(set(word))
        for i in a:
            if i.upper() in a and i.lower() in a:
                if i.lower() not in word[word.index(i.upper()):]:
                    r+=1
        return r//2
