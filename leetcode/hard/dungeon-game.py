class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        import sys
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = sys.maxint
        for j in range(n + 1):
            dp[m][j] = sys.maxint

        dp[m][n - 1] = 0
        dp[m - 1][n] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(
                    min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 0)

        return dp[0][0] + 1


if __name__ == '__main__':
    s = Solution()
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    r = s.calculateMinimumHP(dungeon)
    print r
