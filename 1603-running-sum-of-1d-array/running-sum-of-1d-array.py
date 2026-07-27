class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        summ=0
        for i in nums:
            summ+=i
            l.append(summ)
        return l    