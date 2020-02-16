class Solution(object):
    def mergeStonesTwo(self, stones):
        # if 2 adjacent piles are merged into 1 pile
        # state: minimum cost merging piles from i to j to 1 pile
        # dp[i][j] = min(sum(stones[i:j+1]) + dp[i][k] + dp[k+1][j]) i <= k < j
        if not stones:
            return 0
        n = len(stones)
        memo = [[0] * (n + 1) for _ in range(n + 1)]

        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]

        # l: length of stones[i:j]
        for l in range(2, n + 1):
            # i: left, j: right
            for i in range(1, n - l + 2):
                j = i + l - 1
                memo[i][j] = float('inf')
                subSum = preSum[j] - preSum[i - 1]
                for k in range(i, j):
                    memo[i][j] = min(memo[i][j],
                                     memo[i][k] + memo[k + 1][j] + subSum)
        return memo[1][n]

    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        # if k consecutive piles are merged into 1 pile
        # state: minimum cost merging piles from i to k to k pile
        # dp[i][j][1] = dp[i][j][K] + sum(stones[i:j + 1])
        # dp[i][j][k] = min(dp[i][mid][1] + dp[mid + 1][j][k - 1])
        # initial state: dp[i][i][1] = 0, other = max
        # final answer: dp[1][len(stones)][1]
        n = len(stones)
        # K - 1 items are removed in each steps
        if (n - 1) % (K - 1) != 0:
            return -1

        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]

        memo = [[[float('inf')] * (K + 1) for _ in range(n + 1)]
                for _ in range(n + 1)]
        for i in range(1, n + 1):
            memo[i][i][1] = 0

        for l in range(2, n + 1):
            for i in range(1, n - l + 2):
                j = i + l - 1
                for k in range(2, K + 1):
                    for m in range(i, j):
                        memo[i][j][k] = min(memo[i][j][k],
                                            memo[i][m][1] + 
                                            memo[m + 1][j][k - 1])
                memo[i][j][1] = memo[i][j][K] + (preSum[j] - preSum[i - 1])
        return memo[1][n][1]

    def mergeStones2(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1

        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]

        memo = [[0] * (n + 1) for _ in range(n + 1)]
        for m in range(K, n + 1):
            for i in range(1, n - m + 2):
                j = i + m - 1
                memo[i][j] = float('inf')
                for k in range(i, j, K - 1):
                    memo[i][j] = min(memo[i][j],
                                     memo[i][k] + memo[k + 1][j])
                if (j - i) % (K - 1) == 0:
                    memo[i][j] += preSum[j] - preSum[i - 1]
        return memo[1][n]


if __name__ == '__main__':
    s = Solution()
    stones = [3, 2, 4, 1]
    r = s.mergeStonesTwo(stones)
    print r
    r = s.mergeStones(stones, 2)
    print r
    r = s.mergeStones2(stones, 2)
    print r
