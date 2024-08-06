class Solution:
    def minimumPushes(self, word: str) -> int:
        a=Counter(word)
        if len(a)<9:
            return len(word)
        r=0
        c=0
        a=dict(sorted(a.items(),key= lambda x:x[1],reverse=True))
        for i,j in a.items():
            c+=1
            r+=ceil(c/8)*j
        return r
