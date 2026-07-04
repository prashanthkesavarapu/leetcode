class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        dp=[0]*(l)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,l):
            dp[i]=cost[i]+min(dp[i-2],dp[i-1])
        return min(dp[l-1],dp[l-2])    