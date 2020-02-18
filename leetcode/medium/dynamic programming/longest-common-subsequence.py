class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n, m = len(text1), len(text2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
        return memo[n][m]


if __name__ == '__main__':
    s = Solution()
    text1 = "abc"
    text2 = "abc"
    r = s.longestCommonSubsequence(text1, text2)
    print r
    text1 = "abc"
    text2 = "def"
    r = s.longestCommonSubsequence(text1, text2)
    print r
    text1 = "abcde"
    text2 = "ace"
    r = s.longestCommonSubsequence(text1, text2)
    print r
    text1 = "bl"
    text2 = "yby"
    r = s.longestCommonSubsequence(text1, text2)
    print r