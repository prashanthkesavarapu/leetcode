from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        c=Counter(t)
        req=len(c)
        length=len(s)
        left=0
        right=0
        formed=0
        wind={}
        ans=float("inf"),None,None

        while right<length:
            char=s[right]
            wind[char]=wind.get(char,0)+1

            if char in c and wind[char]==c[char]:
                formed+=1

            while left<=right and formed==req:
                char=s[left]    

                if right-left+1<ans[0]:
                    ans=(right-left+1,left,right)

                wind[char]-=1

                if char in c and wind[char]<c[char]:
                    formed-=1
                left+=1
            right+=1
        return "" if ans[0]==float("inf") else s[ans[1] : ans[2]+1]                



        