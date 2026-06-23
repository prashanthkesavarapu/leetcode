class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        pos =set()
        neg=set()
        board=[["."]*n for _ in range(n)]
        res=[]
        def dfs(r):
            if r==n:
                copy=["".join(r) for r in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue
                board[r][c]="Q"
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)

                dfs(r+1)    
                board[r][c]="."
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        dfs(0)
        return res            
