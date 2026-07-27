class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        maxx=nums[0]
        for i in nums:
            curr=max(i,curr+i)
            maxx=max(curr,maxx)
        return maxx    

