class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxx=0
        for i in range(len(height)):
            while l<r:
                w=r-l
                h=min(height[l],height[r])
                area=h*w
                maxx=max(area,maxx)
                if height[l]<height[r]:
                    l+=1
                else:
                    r-=1
        return maxx                