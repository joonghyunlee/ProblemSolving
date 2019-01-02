class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        def toHexadecimal(n):
            if n < 10:
                return chr(ord('0') + n)
            return chr(ord('a') + n - 10)
        MAX = 0xFFFFFFFF
        MASK = 0xF
        s = []
        d = 0
        while (num & MAX) > 0:
            s.insert(0, toHexadecimal(num & MASK))
            num = (num & MAX) >> 4

        if not s:
            s.append('0')

        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    r = s.toHex(14)
    print r
    r = s.toHex(0)
    print r
    r = s.toHex(16)
    print r
    r = s.toHex(-1)
    print r
