class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        memo = [[0] * N for _ in range(N)]
        memo[r][c] = 1
        moves = ((2,1),(2,-1),(-2,1),(-2,-1),
                 (1,2),(1,-2),(-1,2),(-1,-2))
        for _ in range(K):
            new = [[0] * N for _ in range(N)]
            for r in range(N):
                for c in range(N):
                    for dr, dc in moves:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            new[r + dr][c + dc] += memo[r][c] / 8.0
            memo = new
        return sum(map(sum, memo))

    def knightProbability2(self, N, K, r, c):
        moves = ((2,1),(2,-1),(-2,1),(-2,-1),
                 (1,2),(1,-2),(-1,2),(-1,-2))
        def helper(n, k, r, c):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1
            rate = 0
            for dr, dc in moves:
                rate += helper(n, k - 1, r + dr, c + dc) / 8.0
            return rate
        return helper(N, K, r, c)

    def knightProbability3(self, N, K, r, c):
        memo = [[[0] * N for _ in range(N)] for _ in range(K + 1)]
        moves = ((2,1),(2,-1),(-2,1),(-2,-1),
                 (1,2),(1,-2),(-1,2),(-1,-2))
        def helper(n, k, r, c):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1
            if memo[k][r][c] != 0:
                return memo[k][r][c]
            rate = 0
            for dr, dc in moves:
                rate += helper(n, k - 1, r + dr, c + dc) / 8.0
            memo[k][r][c] = rate
            return rate
        return helper(N, K, r, c)


if __name__ == '__main__':
    s = Solution()
    r = s.knightProbability(3, 2, 0, 0)
    print r
    r = s.knightProbability2(3, 2, 0, 0)
    print r
    r = s.knightProbability3(3, 2, 0, 0)
    print r
    r = s.knightProbability(1, 0, 0, 0)
    print r
    r = s.knightProbability2(1, 0, 0, 0)
    print r
    r = s.knightProbability3(1, 0, 0, 0)
    print r
    r = s.knightProbability(3, 3, 0, 0)
    print r
    r = s.knightProbability2(3, 3, 0, 0)
    print r
    r = s.knightProbability3(3, 3, 0, 0)
    print r
    r = s.knightProbability(3, 2, 0, 0)
    print r
    r = s.knightProbability2(3, 2, 0, 0)
    print r
    r = s.knightProbability3(3, 2, 0, 0)
    print r
