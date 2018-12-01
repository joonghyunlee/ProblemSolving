class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False

        if num == 1:
            return True

        if num & (num - 1):
            return False

        if len(bin(num)[2:]) % 2 == 0:
            return False

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isPowerOfFour(0)
    print r
    r = s.isPowerOfFour(1)
    print r
    r = s.isPowerOfFour(256)
    print r
