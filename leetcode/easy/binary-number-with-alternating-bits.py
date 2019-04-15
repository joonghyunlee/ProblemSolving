class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = (((n << 1) + ((n + 1) & 1)) ^ n)
        return (m + 1) & m == 0


if __name__ == '__main__':
    s = Solution()
    r = s.hasAlternatingBits(5)
    print(r)
    r = s.hasAlternatingBits(4)
    print(r)
    r = s.hasAlternatingBits(21)
    print(r)
