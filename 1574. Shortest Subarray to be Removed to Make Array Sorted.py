class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        a=float("inf")
        p1=0
        while p1<n-1 and arr[p1]<=arr[p1+1]:
            p1+=1
        if p1==n-1:
            return 0
        p2=n-1
        while p2>0 and arr[p2]>=arr[p2-1]:
            p2-=1
        a=min(n-p1-1,p2)
        l=0
        r=p2
        while l<=p1 and r<n:
            if arr[l]<=arr[r]:
                l+=1
            else:
                r+=1
            a=min(a,r-l)
        return a
