class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        signed = None
        num = None
        for c in s:
            if signed is None:
                if c == '+':
                    signed = True
                elif c == '-':
                    signed = False
                elif c in '0123456789':
                    signed = True
                    num = ord(c) - ord('0')
                elif c == ' ':
                    continue
                else:
                    break
            elif c in '0123456789':
                if num is None:
                    num = 0
                num *= 10
                num += ord(c) - ord('0')
            else:
                break

        if num is None:
            return 0
        if num >= 0x80000000:
            num = 0x80000000 - 1
        return num if signed else -num


if __name__ == '__main__':
    s = Solution()
    r = s.myAtoi('42')
    print r
    r = s.myAtoi('      -42')
    print r
    r = s.myAtoi('4193 with words')
    print r
    r = s.myAtoi('words and 987')
    print r
    r = s.myAtoi('-91283472332')
    print r
    r = s.myAtoi('-')
    print r
    r = s.myAtoi('+-2')
    print r
    r = s.myAtoi('987+456')
    print r
    r = s.myAtoi('  + 0 123')
    print r
