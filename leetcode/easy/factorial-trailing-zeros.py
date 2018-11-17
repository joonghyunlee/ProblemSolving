class Solution(object):
    def trailingZeroes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        c2 = 0
        c5 = 0
        for i in range(1, n + 1):
            while i % 2 == 0:
                i /= 2
                c2 += 1
            while i % 5 == 0:
                i /= 5
                c5 += 1

        return min(c2, c5)

    def factorial(self, n):
        r = 1
        for i in range(1, n + 1):
            r *= i
        print r

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        while n > 0:
            s += (n // 5)
            n //= 5
        return s


if __name__ == '__main__':
    s = Solution()
    r = s.trailingZeroes(0)
    print r
    r = s.trailingZeroes(3)
    print r
    r = s.trailingZeroes(5)
    print r
    r = s.trailingZeroes(42)
    print r
    r = s.trailingZeroes(50)
    print r
    r = s.trailingZeroes(1808548329)
    print r
