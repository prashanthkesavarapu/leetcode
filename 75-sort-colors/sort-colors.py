class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=m=0
        r=len(n)-1
        while m<=r:
            if n[m]==0:
                n[l],n[m]=n[m],n[l]
                l+=1
                m+=1
            elif n[m]==1:
                m+=1
            else:
                n[m],n[r]=n[r],n[m]
                r-=1
