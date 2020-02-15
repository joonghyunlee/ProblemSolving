class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [[0] * n for _ in xrange(n)]
        for l in range(n - 1, -1 , -1):
            memo[l][l] = 1
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    if r - l == 1 or memo[l + 1][r - 1]:
                        memo[l][r] = 1
        return sum(map(sum, memo))

    def countSubstrings2(self, s):
        # n: the length of string s
        # 2n - 1: possible positions of the center
        # a   b   c
        # 0 1 2 3 4
        n = len(s)
        total = 0
        for center in xrange(2 * n - 1):
            l = center // 2
            r = l + center % 2
            while l >= 0 and r < n and s[l] == s[r]:
                total += 1
                l, r = l - 1, r + 1
        return total


if __name__ == '__main__':
    s = Solution()
    r = s.countSubstrings('abc')
    print r
    r = s.countSubstrings2('abc')
    print r
    r = s.countSubstrings('aaa')
    print r
    r = s.countSubstrings2('aaa')
    print r