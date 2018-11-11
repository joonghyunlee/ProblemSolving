class Solution(object):
    def addBinary(self, a, b):
        def toInt(s):
            r = 0
            for c in s:
                r *= 2
                if c == '1':
                    r += 1
            return r

        def toStr(n):
            s = []
            while n > 0:
                s.insert(0, n % 2)
                n //= 2
            if not s:
                s = [0]
            return ''.join([str(c) for c in s])

        na = toInt(a)
        nb = toInt(b)
        nr = na + nb
        return toStr(nr)


if __name__ == '__main__':
    s = Solution()
    r = s.addBinary('10', '11')
    print(r)
    r = s.addBinary('11', '1')
    print(r)
    r = s.addBinary('1010', '1011')
    print(r)
    r = s.addBinary('0', '0')
    print(r)
