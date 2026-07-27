class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b=set()
        left=0
        maxx=0
        for i in range(len(s)):
            while s[i] in b:
                b.remove(s[left])
                left+=1
            b.add(s[i])
            maxx=max(maxx,i-left+1)
        return maxx    
