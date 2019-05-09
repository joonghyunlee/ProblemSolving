class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        m = [0] * (n + 1)
        for i in range(n, -1, -1):
            if i == n:
                m[i] = 1
            elif i == n - 1:
                m[i] = 1 if s[i] != '0' else 0
            elif s[i] == '0':
                continue
            elif ((s[i] == '1' and s[i + 1] in '0123456789') or
                  (s[i] == '2' and s[i + 1] in '0123456')):
                m[i] = m[i + 1] + m[i + 2]
            else:
                m[i] = m[i + 1]
        return m[0]


if __name__ == '__main__':
    s = Solution()
    r = s.numDecodings('0')
    print r
    r = s.numDecodings('17')
    print r
