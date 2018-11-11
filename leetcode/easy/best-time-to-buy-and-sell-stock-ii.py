class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = [0]
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i-1])

        profit = 0
        for d in diff:
            if d > 0:
                profit += d

        return profit


if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit([7, 1, 5, 3, 6, 4])
    print r
    r = s.maxProfit([1, 2, 3, 4, 5])
    print r
    r = s.maxProfit([7, 6, 4, 3, 1])
    print r
