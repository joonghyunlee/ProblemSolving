class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n, m = len(s1), len(s2)
        # memo[i][j]: the answer to the problem for the strings s1[i:], s[j:]
        memo = [[0] * (m + 1) for _ in range(n + 1)]

        # When one of the input strings is empty, the answer is the ASCII-sum of the other string. 
        for i in range(n - 1, -1, -1):
            memo[i][m] = memo[i + 1][m] + ord(s1[i])
        for j in range(m - 1, -1, -1):
            memo[n][j] = memo[n][j + 1] + ord(s2[j])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # When s1[i] == s2[j], it can be ignored.
                if s1[i] == s2[j]:
                    memo[i][j] = memo[i + 1][j + 1]
                else:
                    memo[i][j] = min(memo[i + 1][j] + ord(s1[i]),
                                     memo[i][j + 1] + ord(s2[j]))

        return memo[0][0]

    def minimumDeleteSum2(self, s1, s2):
        n, m = len(s1), len(s2)
        memo = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    memo[i + 1][j + 1] = memo[i][j] + ord(s1[i])
                else:
                    memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])
        return sum(map(ord, s1 + s2)) - memo[n][m] * 2


if __name__ == '__main__':
    s = Solution()
    r = s.minimumDeleteSum('sea', 'eat')
    print r
    r = s.minimumDeleteSum2('sea', 'eat')
    print r
    r = s.minimumDeleteSum('delete', 'leet')
    print r
    r = s.minimumDeleteSum2('delete', 'leet')
    print r
    r = s.minimumDeleteSum('sjfqkfxqoditw', 'fxymelgo')
    print r
    r = s.minimumDeleteSum2('sjfqkfxqoditw', 'fxymelgo')
    print r
