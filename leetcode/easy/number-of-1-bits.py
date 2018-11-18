class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        w = 0
        while n > 0:
            w += n % 2
            n //= 2
        return w


if __name__ == '__main__':
    s = Solution()
    r = s.hammingWeight(11)
    print r
    r = s.hammingWeight(0)
    print r
    r = s.hammingWeight(2)
    print r
    r = s.hammingWeight(128)
    print r
