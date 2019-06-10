class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = []
        roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        while num > 0:
            for val, c in roman:
                if num >= val:
                    num -= val
                    ret.append(c)
                    break
        return ''.join(ret)


if __name__ == '__main__':
    s = Solution()
    r = s.intToRoman(3)
    print r
    r = s.intToRoman(4)
    print r
    r = s.intToRoman(9)
    print r
    r = s.intToRoman(58)
    print r
    r = s.intToRoman(1994)
    print r
