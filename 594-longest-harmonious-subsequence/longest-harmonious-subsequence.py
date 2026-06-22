from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c=Counter(nums)
        maxx=0
        for i in c:
            if i+1 in c:
                length=c[i]+c[i+1]
                maxx=max(maxx,length)
        return maxx        
