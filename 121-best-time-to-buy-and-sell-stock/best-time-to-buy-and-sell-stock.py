class Solution:
    def maxProfit(self, n: List[int]) -> int:
        left=0
        maxx=0
        for i in range(1,len(n)):
            if n[i]<n[left]:
                left=i
            price=n[i]-n[left]
            maxx=max(maxx,price)
        return maxx        