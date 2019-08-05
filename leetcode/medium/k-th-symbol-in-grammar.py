class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        # N: 0 .... K
        # N - 1: 0 .... K // 2
        def helper(n, k):
            if n == 0 and k == 0:
                return 0
            return helper(n - 1, k // 2) ^ (k & 1)

        return helper(N - 1, K - 1)


if __name__ == '__main__':
    s = Solution()
    r = s.kthGrammar(1, 1)
    print r
    r = s.kthGrammar(2, 1)
    print r
    r = s.kthGrammar(2, 2)
    print r
    r = s.kthGrammar(4, 5)
    print r
