class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=float('inf')
        profit=0
        for i in prices:
            minp=min(minp,i)
            profit=max(profit,i-minp)
        return profit