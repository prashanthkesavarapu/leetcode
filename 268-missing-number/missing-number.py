class Solution(object):
    def missingNumber(self, nums):
        a=sum(nums)
        n=len(nums)
        actual=n*(n+1)//2 -a
        return actual
