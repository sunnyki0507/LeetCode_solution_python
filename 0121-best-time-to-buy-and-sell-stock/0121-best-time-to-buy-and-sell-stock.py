class Solution(object):
    def maxProfit(self, prices):

        profit = 0
        buy = prices[0]

        for i in prices[1:]:
            if buy > i:
                buy = i
            profit = max(profit, i - buy)
        return profit

        #my code
        # maxN = 0
        # buy = max(prices)
        # for i in range(len(prices) - 1):
        #     if buy <= prices[i]:
        #         continue
        #     buy = prices[i]
        #     sell = max(prices[i+1:])
        #     if (sell - buy) > maxN:
        #         maxN = sell - buy
        # return maxN


        """
        :type prices: List[int]
        :rtype: int
        """
        