class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=curr_min=res=nums[0]
        for i in nums[1:]:
            if i<0:
                curr_max,curr_min=curr_min,curr_max
            curr_max=max(i,curr_max*i)
            curr_min=min(i,curr_min*i)

            res=max(res,curr_max)
        return res        

        