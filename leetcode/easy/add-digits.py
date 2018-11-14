class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 0:
            return 0

        s = 0
        while num > 0:
            s = s + (num % 10)
            if s >= 10:
                s -= 9
            num //= 10
        return s


if __name__ == '__main__':
    s = Solution()
    r = s.addDigits(456)
    print(r)
    r = s.addDigits(1)
    print(r)
    r = s.addDigits(728940)
    print(r)
    r = s.addDigits(100)
    print(r)
    r = s.addDigits(19)
    print(r)
