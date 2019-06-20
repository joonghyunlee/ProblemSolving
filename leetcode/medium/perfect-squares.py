class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def helper(n):
            if n < 4:
                return n
            r = int(math.sqrt(n))
            rr = int(math.sqrt(r))
            mi = n
            for i in range(r, rr, -1):
                q = n // (i ** 2)
                re = n % (i ** 2)
                mi = min(mi, q + helper(re))
            return mi
        return helper(n)


if __name__ == '__main__':
    s = Solution()
    r = s.numSquares(12)
    print(r)
    r = s.numSquares(13)
    print(r)
    r = s.numSquares(345)
    print(r)
    r = s.numSquares(45678)
    print(r)
