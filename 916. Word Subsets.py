class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = collections.Counter()
        for i in words2:
            count |= collections.Counter(i)
        return [a for a in words1 if not count - Counter(a)]
