class Solution(object):
    def maxProfit(self, n):
        price=0
        maxx=0
        left=0
        for i in range(1,len(n)):
            if n[i]<n[left]:
                left=i
            price=n[i]-n[left]
            maxx=max(maxx,price)

        return maxx    