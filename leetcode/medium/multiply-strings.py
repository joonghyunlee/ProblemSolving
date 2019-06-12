class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def helper(n, m):
            su = 0
            for c in n:
                d = ord(c) - ord('0')
                su *= 10
                su += (d * (ord(m) - ord('0')))
            return su
        ret = 0
        for c in num2:
            ret *= 10
            ret += helper(num1, c)
        return str(ret)


if __name__ == '__main__':
    s = Solution()
    r = s.multiply('2', '3')
    print(r)
    r = s.multiply('123', '456')
    print(r)
