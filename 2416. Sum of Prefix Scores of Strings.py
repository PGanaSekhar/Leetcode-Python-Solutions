class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        a=defaultdict(int)
        for i in words:
            for j in range(len(i)):
                a[i[:j+1]]+=1
        r=[]
        for i in words:
            s=0
            for j in range(len(i)):
                s+=a[i[:j+1]]
            r.append(s)
        return r
