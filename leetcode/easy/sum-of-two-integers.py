class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        MASK = 0xFFFFFFFF
        c = 0
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)


if __name__ == '__main__':
    s = Solution()
    r = s.getSum(-12, -8)
    print r
