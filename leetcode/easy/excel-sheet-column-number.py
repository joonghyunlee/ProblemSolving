class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for c in s:
            n *= 26
            d = ord(c) - ord('A')
            n += d + 1

        return n


if __name__ == '__main__':
    s = Solution()
    r = s.titleToNumber('A')
    print r
    r = s.titleToNumber('AB')
    print r
    r = s.titleToNumber('ZY')
    print r
