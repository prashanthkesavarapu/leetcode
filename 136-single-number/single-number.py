class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1    
        for i in nums:
            if a[i]==1:
                return i
                break