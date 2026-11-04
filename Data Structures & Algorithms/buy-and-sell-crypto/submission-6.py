class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        pro = 0

        for price in prices:
            buy = min(buy, price)
            pro = max(pro, price - buy)

        return pro