class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n] if n >= 1 else 0


if __name__ == '__main__':
    s = Solution()
    r = s.numTrees(1)
    print(r)
    r = s.numTrees(2)
    print(r)
    r = s.numTrees(3)
    print(r)
    r = s.numTrees(5)
    print(r)
    r = s.numTrees(19)
    print(r)
