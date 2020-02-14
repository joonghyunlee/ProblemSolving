class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        memo = {}
        def helper(num, i, j):
            if not (i >= 0 and i < m and j >= 0 and j < n):
                return 1
            elif num <= 0:
                return 0

            if (num, i, j) in memo:
                return memo[(num, i, j)]

            total = (helper(num - 1, i - 1, j) +
                     helper(num - 1, i + 1, j) +
                     helper(num - 1, i, j - 1) +
                     helper(num - 1, i, j + 1))
            memo[(num, i, j)] = total
            return total
        return helper(N, i, j) % (pow(10, 9) + 7)

    def findPaths2(self, m, n, N, i, j):
        M = pow(10, 9) + 7
        nextMap = [[0] * n for _ in range(m)]
        nextMap[i][j] = 1
        total = 0
        for _ in range(1, N + 1):
            currMap = nextMap
            nextMap = [[0] * n for _ in range(m)]
            for r, row in enumerate(currMap):
                for c, val in enumerate(row):
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            nextMap[nr][nc] += val
                            nextMap[nr][nc] %= M
                        else:
                            total += val
                            total %= M
        return total


if __name__ == '__main__':
    s = Solution()
    print s.findPaths2(2, 2, 2, 0, 0)
    print s.findPaths2(1, 3, 3, 0, 1)
    print s.findPaths2(8, 4, 10, 5, 0)
    print s.findPaths2(8, 7, 16, 1, 5)
    print s.findPaths2(8, 50, 23, 5, 26)