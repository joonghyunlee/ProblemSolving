class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        tq, thq, fq = [2], [3], [5]
        un = 1
        for i in range(n - 1):
            mi = min(tq[-1], thq[-1], fq[-1])
            if mi == tq[-1]:
                ne = tq.pop()
                tq.insert(0, ne * 2)
                thq.insert(0, ne * 3)
                fq.insert(0, ne * 5)
            elif mi == thq[-1]:
                ne = thq.pop()
                thq.insert(0, ne * 3)
                fq.insert(0, ne * 5)
            else:
                ne = fq.pop()
                fq.insert(0, ne * 5)
            un = ne

        return un


if __name__ == '__main__':
    s = Solution()
    r = s.nthUglyNumber(10)
    print(r)
