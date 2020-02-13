class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [[0] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            memo[l][l] = 1
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    memo[l][r] = memo[l + 1][r - 1] + 2
                else:
                    memo[l][r] = max(memo[l + 1][r], memo[l][r - 1])
        return memo[0][n - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindromeSubseq('bbbab')
    print r