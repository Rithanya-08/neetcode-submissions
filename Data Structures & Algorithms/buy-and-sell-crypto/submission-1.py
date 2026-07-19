class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        for i in range(len(prices)-1,-1,-1):
            for j in range(i,-1,-1):
                maxx = max(maxx,prices[i]-prices[j])

        return maxx