class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos = set() 
        neg = set()
        
        self.count = 0
        
        def dfs(r):
            if r == n:
                self.count += 1
                return
                
            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue
                    
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)
                
                dfs(r+1)
                
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                
        dfs(0)
        return self.count