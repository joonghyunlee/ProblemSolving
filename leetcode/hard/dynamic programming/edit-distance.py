class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            memo[i][0] = i
        for i in range(m + 1):
            memo[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = min(memo[i - 1][j],
                                     memo[i][j - 1],
                                     memo[i - 1][j - 1]) + 1
        return memo[n][m]

    def minDistance2(self, word1, word2):
        def helper(w1, w2):
            if not w1 and not w2:
                return 0
            elif not w1:
                return len(w2)
            elif not w2:
                return len(w1)
            elif w1[0] == w2[0]:
                return helper(w1[1:], w2[1:])
            return min(1 + helper(w1, w2[1:]),
                       1 + helper(w1[1:], w2),
                       1 + helper(w1[1:], w2[1:]))
        return helper(word1, word2)


if __name__ == '__main__':
    s = Solution()
    r = s.minDistance("horse", "ros")
    print r
    r = s.minDistance2("horse", "ros")
    print r
    r = s.minDistance("intention", "execution")
    print r
    r = s.minDistance2("intention", "execution")
    print r