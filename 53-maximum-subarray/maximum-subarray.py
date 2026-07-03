class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=nums[0]
        curr=0
        for i in nums:
            curr+=i
            if curr>maxx:
                maxx=curr
            if curr<0:
                curr=0
        return maxx        


