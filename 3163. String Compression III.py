class Solution:
    def compressedString(self, word: str) -> str:
        r=""
        t=0
        t1=word[0]
        for i in word:
            if i==t1:
                t+=1
            else:
                while t>9:
                   r+="9"+t1
                   t-=9
                r+=str(t)+t1
                t1=i
                t=1
        while t>9:
            r+="9"+t1
            t-=9
        r+=str(t)+t1
        return r
