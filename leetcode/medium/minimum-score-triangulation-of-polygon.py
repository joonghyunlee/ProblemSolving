import sys

from functools import reduce


class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def helper(A, start, end):
            if end - start + 1 < 3:
                return 0
            if memo[start][end] is not None:
                return memo[start][end]

            m = sys.maxsize
            for k in range(start + 1, end):
                p = A[start] * A[end] * A[k] + \
                    helper(A, start, k) + helper(A, k, end)
                if p < m:
                    m = p

            memo[start][end] = m
            return m

        n = len(A)
        memo = [[None] * n for i in range(n)]

        return helper(A, 0, len(A) - 1)


if __name__ == '__main__':
    s = Solution()
    r = s.minScoreTriangulation([3, 7, 4, 5])
    print r
    r = s.minScoreTriangulation([1, 3, 1, 4, 1, 5])
    print r
    r = s.minScoreTriangulation([22, 17, 68, 3, 88, 59, 54, 23, 22, 77])
    print r
