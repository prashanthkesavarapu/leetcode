class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max=curr_min=0
        g_max=g_min=nums[0]
        t=0
        for i in nums:
            curr_max=max(i,curr_max+i)
            g_max=max(g_max,curr_max)
            t+=i
            curr_min=min(i,curr_min+i)
            g_min=min(g_min,curr_min)
        if g_max<0:
            return g_max
        return max(g_max,t-g_min)    