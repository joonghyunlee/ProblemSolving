class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 


if __name__ == '__main__':
    s = Solution()
    print s.coinChange([1, 2, 5], 11)
    print s.coinChange([2], 3)
    print s.coinChange([2, 5, 10, 1], 27)
    print s.coinChange([186, 419, 83, 408], 6249)