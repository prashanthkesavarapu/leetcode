from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        c=Counter(nums)

        for v in c.values():
            if v>1:
                return True
        return False       

        