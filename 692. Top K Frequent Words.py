class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        r=[]
        a={}
        for i in set(words):
            t=words.count(i)
            if t not in a:
                a[t]=[i]
            else:
                a[t].append(i)
                a[t].sort()
        a=dict(sorted(a.items())[::-1])
        for i,j in a.items():
            r[:]=r+j                    
            if len(r)>=k:
                return r[:k]
