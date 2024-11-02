class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start,goal=min(start,goal),max(start,goal)
        a=bin(start)[2:]
        b=bin(goal)[2:]
        a='0'*(len(b)-len(a))+a
        r=0
        for i in range(len(a)):
            r+=int(a[i]!=b[i])
        return r
