class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = max(prices[j] - prices[i], profit)

        return profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def subMaxProfit(nums, i, j):
            if i >= j:
                return 0

            lprofit = subMaxProfit(nums, i, (i+j)//2)
            rprofit = subMaxProfit(nums, (i+j)//2 + 1, j)

            lmin = nums[i]
            for x in range(i+1, (i+j)//2 + 1):
                lmin = min(lmin, nums[x])
            rmax = nums[(i+j)//2 + 1]
            for x in range((i+j)//2 + 2, j + 1):
                rmax = max(rmax, nums[x])

            return max(lprofit, rprofit, rmax - lmin)

        return subMaxProfit(prices, 0, len(prices) - 1)


if __name__ == '__main__':
    s = Solution()
    # r = s.maxProfit2([7, 1, 5, 3, 6, 4])
    # print(r)
    # r = s.maxProfit2([7, 6, 3, 2, 1])
    # print(r)
    # r = s.maxProfit2([2, 1, 4])
    # print(r)
    r = s.maxProfit2([6, 1, 3, 2, 4, 7])
    print(r)
