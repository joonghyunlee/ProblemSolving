class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num % 5 == 0 and num >= 5:
            num //= 5
        while num % 3 == 0 and num >= 3:
            num //= 3
        while num % 2 == 0 and num >= 2:
            num //= 2
        if num != 1:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(6))
    print(s.isUgly(8))
    print(s.isUgly(14))
    print(s.isUgly(1))
    print(s.isUgly(230))
    print(s.isUgly(65536 * 5))
