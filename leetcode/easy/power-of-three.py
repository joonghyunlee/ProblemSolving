class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 == 0:
            return False

        if n % 10 not in [3, 9, 7, 1]:
            return False

        d = 1
        while d < n:
            d *= 3

        if d != n:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isPowerOfThree(243)
    print r
