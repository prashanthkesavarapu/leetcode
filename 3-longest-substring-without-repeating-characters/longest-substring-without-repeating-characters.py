class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wind=set()
        maxl=0
        left=0
        for i in range(len(s)):
            while s[i] in wind:
                wind.remove(s[left])
                left+=1
            wind.add(s[i])    
            maxl=max(maxl,i-left+1)
        return maxl        