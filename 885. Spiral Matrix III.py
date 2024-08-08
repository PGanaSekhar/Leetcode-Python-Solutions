class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[[0,1],[1,0],[0,-1],[-1,0]] #trick
        r=[]
        rs,cs=rStart,cStart
        i=0
        s=1
        while len(r)<rows*cols:
            for j in range(2):
                a,b=directions[i]
                for k in range(s):
                    if 0<=rs<rows and 0<=cs<cols:
                        r.append([rs,cs])
                    rs,cs=rs+a,cs+b
                i=(i+1)%4
            s+=1
        return r
