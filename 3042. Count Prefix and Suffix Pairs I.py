class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        r=0
        for i,j in list(combinations(words,2)):
            if len(i)>len(j):
                pass
            if j[:len(i)]==i and j[-len(i):]==i:
                r+=1
        return r
