class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        co = n // 2
        memo = [[float('inf')] * (n + 1) for _ in range(co + 1)]
        memo[0][1] = 0
        for r in range(1, co + 1):
            for i in range (0, r):
                memo[r][r] = min(memo[r][r], memo[i][r])
            memo[r][r] += 1

            for c in range(r + r, n + 1, r):
                memo[r][c] = memo[r][c - r] + 1
        return min(map(lambda x: x[-1], memo))

    def minSteps2(self, n):
        memo = [float('inf')] * (n + 1)
        memo[1] = 0
        for r in range(1, n // 2 + 1):
            memo[r] += 1
            for c in range(r + r, n + 1, r):
                memo[c] = memo[c - r] + 1
        return memo[n]

    def minSteps3(self, n):
        # n = 18
        # 18 * A = (9 * A) * 2
        # 9 * A = (3 * A) * 3
        # 3 * A = A * 3
        ans = 0
        for i in range(2, n + 1):
            while n % i == 0:
                ans += i
                n //= i
        return ans

    def minSteps4(self, n):
        memo = [0] * (n + 1)
        for i in range(2, n + 1):
            memo[i] = i # maximum case
            for j in range(i // 2, 1, -1):
                if i % j == 0:
                    memo[i] = memo[j] + (i // j)
                    break
        return memo[n]


if __name__ == '__main__':
    s = Solution()
    r = s.minSteps(3)
    print r
    r = s.minSteps2(3)
    print r
    r = s.minSteps3(3)
    print r
    r = s.minSteps4(3)
    print r
    r = s.minSteps(4)
    print r
    r = s.minSteps2(4)
    print r
    r = s.minSteps3(4)
    print r
    r = s.minSteps4(4)
    print r
    r = s.minSteps(741)
    print r
    r = s.minSteps2(741)
    print r
    r = s.minSteps3(741)
    print r
    r = s.minSteps4(741)
    print r