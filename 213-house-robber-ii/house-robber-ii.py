class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return nums[0]
        def mini(n):
            if len(n) ==1:
                return n[0]
            dp=[0]*len(n)
            dp[0]=n[0]
            dp[1]=max(n[0],n[1])
            for i in range(2,len(n)):
                dp[i]=max(dp[i-2]+n[i],dp[i-1])
            return dp[-1]           
        return max(mini(nums[:-1]),mini(nums[1:]))        