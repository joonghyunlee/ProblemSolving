class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = 1
        while d < n: d *= 2

        return True if d == n else False


if __name__ == '__main__':
    s = Solution()
    r = s.isPowerOfTwo(1)
    print(r)
    r = s.isPowerOfTwo(16)
    print(r)
    r = s.isPowerOfTwo(216)
    print(r)
