class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        counter = collections.Counter({0:1})
        res = s = 0
        for i in A:
            s += i
            res += counter[s-S]
            counter[s] += 1
        return res
