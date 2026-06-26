class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        wind=0
        maxl=float('inf')
        for right in range(len(nums)):
            wind+=nums[right]
            while wind>=target:
                maxl=min(maxl,right-left+1)
                wind-=nums[left]
                left+=1  
        return maxl if maxl!=float('inf') else 0
        