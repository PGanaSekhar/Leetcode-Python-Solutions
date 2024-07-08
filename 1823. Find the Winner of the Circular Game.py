class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=[i for i in range(1,n+1)]
        j=0
        for i in range(n-1):
            b=a[(j+k)%len(a)]
            a.pop((j+k-1)%len(a))
            j=a.index(b)
        return a[0]
