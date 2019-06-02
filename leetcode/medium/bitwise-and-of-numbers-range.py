# 4: 0100
# 5: 0101
# 6: 0110
# 7: 0111
# 8: 1000
# 100100010011
# 100100010100


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        distance = n - m
        mask = 0b1
        ret = m & n
        while mask <= ret:
            if mask & ret:
                if (mask - ((mask - 1) & m)) <= distance:
                    ret ^= mask
            mask <<= 1
        return ret


if __name__ == '__main__':
    s = Solution()
    r = s.rangeBitwiseAnd(7, 12)
    print r
    r = s.rangeBitwiseAnd(1, 1)
    print r
    r = s.rangeBitwiseAnd(6, 8)
    print r
