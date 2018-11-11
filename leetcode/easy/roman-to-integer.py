class Solution(object):
    def romanToInt(self, s):
        ROMAN_TO_INT = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        digit = 0
        for c in s:
            digit = digit + ROMAN_TO_INT[c]

        if s.find('IV') >= 0 or s.find('IX') >= 0:
            digit = digit - 2

        if s.find('XL') >= 0 or s.find('XC') >= 0:
            digit = digit - 20

        if s.find('CD') >= 0 or s.find('CM') >= 0:
            digit = digit - 200

        return digit


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('IV'))
    print(s.romanToInt('IX'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))
