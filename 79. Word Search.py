class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        p=set()

        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=row or c>=col or (r,c) in p or word[i]!=board[r][c]:
                return False
            p.add((r,c))
            res=(dfs(r,c-1,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r+1,c,i+1))
            p.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
