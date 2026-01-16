class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for i in prices[1:]:
            if buy > i:
                buy = i
            if i > buy:
                profit += i - buy
                buy = i
        return profit
                
            
            
    

        """
        :type prices: List[int]
        :rtype: int
        """
        