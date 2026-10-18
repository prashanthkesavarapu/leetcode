class Solution(object):
    def moveZeroes(self, nums):
        d=[]
        zeros=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            else:
                zeros+=1
        for i in range(zeros):
            nums[j]=0
            j+=1            