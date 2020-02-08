class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        ans, base = 10, 9
        for i in range(2, min(n, 10) + 1):
            base = base * (9 - i + 2)
            ans += base

        return ans


if __name__ == '__main__':
    s = Solution()
    print s.countNumbersWithUniqueDigits(2)
    print s.countNumbersWithUniqueDigits(3)
    print s.countNumbersWithUniqueDigits(14)