class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 1:
            return dividend
        if dividend == -0x80000000 and divisor == -1:
            return 0x80000000 - 1

        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        ret = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while temp <= dividend:
                dividend -= temp
                ret += i
                temp <<= 1
                i <<= 1

        return -ret if negative else ret


if __name__ == '__main__':
    s = Solution()
    r = s.divide(7, 3)
    print r
    r = s.divide(10, 3)
    print r
    r = s.divide(7, -3)
    print r
