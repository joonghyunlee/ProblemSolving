class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def comb(e, l, r, n):
            if n == 0:
                return [0]
            if n == 1:
                return e[l:r]
            res = []
            for i in range(l, r-n+1):
                sub = comb(e, i+1, r, n-1)
                for j in sub:
                    res.append(e[i] + j)
            return res

        elems = [2 ** x for x in range(10)]
        combs = sorted(comb(elems, 0, 10, num))
        hmask, mmask = 0b1111 << 6, 0b111111
        times = []
        for c in combs:
            hour = (c & hmask) >> 6
            min = c & mmask
            if hour > 11 or min > 59:
                continue
            times.append("%d:%02d" % (hour, min))
        return times


if __name__ == '__main__':
    s = Solution()
    r= s.readBinaryWatch(2)
    print(r)
    r= s.readBinaryWatch(0)
    print(r)
