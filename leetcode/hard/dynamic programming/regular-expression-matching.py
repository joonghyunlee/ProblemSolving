class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, p):
            if not p:
                return not s
            firstMatch = bool(s) and p[0] in (s[0], '.')
            if len(p) >= 2 and p[1] == '*':
                return (helper(s, p[2:]) or
                        firstMatch and helper(s[1:], p))
            else:
                return firstMatch and helper(s[1:], p[1:])
        return helper(s, p)

    def isMatch2(self, s, p):
        memo = {}
        def helper(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if j == len(p):
                memo[i, j] = i == len(s)
            else:
                firstMatch = i < len(s) and p[j] in (s[i], '.')
                if j + 1 < len(p) and p[j + 1] == '*':
                    memo[i, j] = (helper(i, j + 2) or 
                                  firstMatch and helper(i + 1, j))
                else:
                    memo[i, j] = firstMatch and helper(i + 1, j + 1)
            return memo[i, j]
        return helper(0, 0)

    def isMatch3(self, s, p):
        # memo[i][j] = 
        # s[i] == p[j] or p[j] == '.': memo[i - 1][j - 1]
        # p[j] == '*': memo[i][j - 2] or
        #              memo[i - 1][j] if s[i] == p[j - 1] or p[j - 1] == '.'
        # False
        memo = [[False] * (len(p) + 1) for _ in xrange(len(s) + 1)]
        # initialize
        # if s is empty string and p contains '*' like 'a*' and 'a*b*', it is always matched.
        # but if p is 'ba*' then it can't be matched.
        memo[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                memo[0][i] = memo[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    memo[i][j] = memo[i - 1][j - 1]
                elif p[j - 1] == '*':
                    memo[i][j] = memo[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        memo[i][j] = memo[i][j] or memo[i - 1][j]
                else:
                    memo[i][j] = False
        print memo
        return memo[len(s)][len(p)]


if __name__ == '__main__':
    s = Solution()
    r = s.isMatch3('aa', 'a')
    print r
    r = s.isMatch3('aa', 'a*')
    print r
    r = s.isMatch3('ab', '.*')
    print r
    r = s.isMatch3('aab', 'c*a*b')
    print r
    r = s.isMatch3('mississippi', 'mis*is*p*.')
    print r
    r = s.isMatch3('ab', '.*c')
    print r
    r = s.isMatch3('a', 'ab*a')
    print r