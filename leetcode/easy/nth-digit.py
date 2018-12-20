class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        def digit(n):
            return 9 * (10 ** (n - 1)) * n
        if n < 10:
            return n
        d, s = 1, 0
        while digit(d) < n:
            s += digit(d)
            d += 1
        m = n - s - 1
        c = str((10 ** (d-1)) + (m//d))
        return int(c[m % d])


if __name__ == '__main__':
    s = Solution()
    r = s.findNthDigit(14)
    print(r)
    r = s.findNthDigit(15)
    print(r)
    r = s.findNthDigit(16)
    print(r)
    r = s.findNthDigit(17)
    print(r)
    r = s.findNthDigit(8)
    print(r)
