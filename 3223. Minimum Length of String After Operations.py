class Solution:
    def minimumLength(self, s: str) -> int:
        if len(set(s))==len(s):
            return len(s)
        return sum([1 if i%2!=0 else 2 for i in Counter(s).values()])
