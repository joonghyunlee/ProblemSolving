class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        b1 = b0 = -prices[0]
        s1, s0 = 0, 0
        for i in range(1, n):
            b0 = max(s1 - prices[i], b1)
            s0 = max(b1 + prices[i] - fee, s1)
            b1, s1 = b0, s0

        return s0


if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print(r)
