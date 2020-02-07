class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * (n + 1)

        def helper(n):
            if n <= 2:
                return 1

            if dp[n]:
                return dp[n]

            maxProduct = 0
            for i in range(1, n // 2 + 1):
                maxProduct = max(maxProduct,
                                 helper(i) * (n - i),
                                 i * helper(n - i),
                                 helper(i) * helper(n - i),
                                 i * (n - i))

            dp[n] = maxProduct

            return dp[n]

        return helper(n)


if __name__ == '__main__':
    s = Solution()
    print s.integerBreak(3)
    print s.integerBreak(44)
