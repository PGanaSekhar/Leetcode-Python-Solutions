class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        g=[]
        for i in matrix:
            g.append(i[:])
        for i in range(len(matrix)):
            j=0
            while 0 in matrix[i][j:]:
                j=matrix[i][j:].index(0)+j
                g[i]=[0]*len(matrix[i])
                for k in range(len(g)):
                    g[k][j]=0
                j+=1
        for i in range(len(g)):
            matrix[i]=g[i]
