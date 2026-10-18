class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Initialize a row of size n with 1s, since there's only 1 way to reach any cell in the first row
        dp = [1] * n
        
        # Iterate through each row starting from the second row
        for _ in range(1, m):
            for j in range(1, n):
                # The current cell value is the sum of the cell to its left and the cell above it
                dp[j] += dp[j - 1]
                
        return dp[-1]