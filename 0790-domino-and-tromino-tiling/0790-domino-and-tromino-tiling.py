class Solution(object):
    def numTilings(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        mod = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n+1):
            dp[i] = dp[i-1] * 2 +dp[i-3] 
        return dp[n] % mod

        """
        :type n: int
        :rtype: int
        """
        