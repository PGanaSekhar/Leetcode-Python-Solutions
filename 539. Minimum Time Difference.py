class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints)!=len(set(timePoints)):
            return 0
        def change(t):
            h,m=t.split(":")
            return (int(h)*60)+int(m)
        a=[]
        l=len(timePoints)
        for i in range(len(timePoints)):
            a.append(change(timePoints[i]))
        a.sort()
        return min(min(abs(a[(i+1)%l]-a[i]),abs(a[(i+1)%l]+(60*24)-a[i]),abs(a[(i+1)%l]-(a[i]+(60*24)))) for i in range(l))
