class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        b=['a','e','i','o','u']
        r=[0]
        a=[]
        t=0
        for i in words:
            if i[0] in b and i[-1] in b:
                t+=1
            r.append(t)
        for i,j in queries:
            a.append(r[j+1]-r[i])
        return a
