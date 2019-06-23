class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import sys
        qs = [0] * len(primes)
        ugs = [1]
        for i in range(n - 1):
            mv, mi = sys.maxsize, 0
            for j, p in enumerate(primes):
                if mv == ugs[qs[j]] * p:
                    qs[j] += 1
                if mv > ugs[qs[j]] * p:
                    mv = ugs[qs[j]] * p
                    mi = j
            ugs.append(mv)
            qs[mi] += 1
        return ugs[-1]


if __name__ == '__main__':
    s = Solution()
    primes = [2, 7, 13, 19]
    r = s.nthSuperUglyNumber(12, primes)
    print r
    primes = [2, 3, 5]
    r = s.nthSuperUglyNumber(2, primes)
    print r
