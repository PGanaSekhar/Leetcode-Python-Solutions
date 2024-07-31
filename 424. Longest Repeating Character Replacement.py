class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a=b=0
        c=Counter()
        for i in range(len(s)):
            c[s[i]]+=1
            a=max(a,c[s[i]])
            if b-a<k:
                b+=1
            else:
                c[s[i-b]]-=1
        return b
