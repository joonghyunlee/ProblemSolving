class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n & 0b11 else False


if __name__ == '__main__':
    s = Solution()
    r = s.canWinNim(4)
    print r
    r = s.canWinNim(5)
    print r
    r = s.canWinNim(6)
    print r
    r = s.canWinNim(7)
    print r
    r = s.canWinNim(8)
    print r
