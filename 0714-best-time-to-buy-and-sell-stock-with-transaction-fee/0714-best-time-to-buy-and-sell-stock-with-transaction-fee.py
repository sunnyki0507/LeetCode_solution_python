class Solution(object):
    def maxProfit(self, prices, fee):
        maxProfit = 0
        mini = max(prices) + 1
        for num in prices:
            if num < mini:
                mini = num
            elif (num - mini) > fee:
                maxProfit += num - mini - fee
                mini = num - fee
        return maxProfit
        
                
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        