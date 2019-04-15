class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def countOne(n):
            mask, count = 0b1, 0
            while n >= mask:
                if n & mask:
                    count += 1
                mask <<= 1
            return count
        ps = [2, 3, 5, 7, 11, 13, 17, 19]
        count = 0
        for i in range(L, R+1):
            c = countOne(i)
            if c in ps:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    r = s.countPrimeSetBits(6, 10)
    print(r)
    r = s.countPrimeSetBits(10, 15)
    print(r)
