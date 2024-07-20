class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r=[[0]*len(colSum) for i in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                r[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=r[i][j]
                colSum[j]-=r[i][j]
        return r
