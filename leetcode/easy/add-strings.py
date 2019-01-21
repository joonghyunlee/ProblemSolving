class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1) - 1, len(num2) - 1
        ret = []
        c = 0
        while n1 >= 0 or n2 >= 0:
            c1 = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
            c2 = ord(num2[n2]) - ord('0') if n2 >= 0 else 0

            n1, n2 = n1 - 1, n2 - 1

            s = c1 + c2 + c
            ret.insert(0, chr(ord('0') + s % 10))
            c = s // 10

        if c > 0:
            ret.insert(0, chr(ord('0') + c))

        return ''.join(ret)


if __name__ == '__main__':
    s = Solution()
    r = s.addStrings('123', '456')
    print(r)
    r = s.addStrings('123456789', '456789123')
    print(r)
    r = s.addStrings('1', '9')
    print(r)
