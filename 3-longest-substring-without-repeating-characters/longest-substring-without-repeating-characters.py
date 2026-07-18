class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wind=set()
        left=0
        maxx=0
        for i in range(len(s)):
            while s[i] in wind:
                wind.remove(s[left])
                left+=1
            wind.add(s[i])
            maxx=max(maxx,i-left+1)
        return maxx        