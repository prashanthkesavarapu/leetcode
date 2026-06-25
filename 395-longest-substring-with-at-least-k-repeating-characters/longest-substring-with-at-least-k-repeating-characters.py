from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0 
        c=Counter(s)
        for i,v in c.items():
            if v<k:
                return max(self.longestSubstring(j,k) for j in s.split(i) )
        return len(s)

        