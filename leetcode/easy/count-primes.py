class Solution(object):
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = range(2, n)
        for i in range(len(nums)):
            d = nums[i]
            if d == 0:
                continue

            for j in range(i + 1, len(nums)):
                if nums[j] % d == 0:
                    nums[j] = 0

        c = 0
        for n in nums:
            if n != 0:
                c +=1

        return c

    def countPrimes(self, n):
        primes = [1 if i > 1 else 0 for i in range(n)]

        import math
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if primes[i] == 0:
                continue
            for j in range(i ** 2, n, i):
                primes[j] = 0
        print primes

        return sum(primes)


if __name__ == '__main__':
    s = Solution()
    r = s.countPrimes1(20)
    print r
    r = s.countPrimes(20)
    print r
    r = s.countPrimes1(10)
    print r
    r = s.countPrimes(10)
    print r

