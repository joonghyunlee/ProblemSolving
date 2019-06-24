class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if n == 0:
                return 1
            elif n < 0:
                return 1 / helper(x, -n)
            elif n % 2 == 1:
                return x * helper(x, n - 1)

            return helper(x * x, n // 2)

        return helper(x, n)


if __name__ == '__main__':
    s = Solution()
    r = s.myPow(2.0, 10)
    print(r)
    r = s.myPow(2.1, 3)
    print(r)
    r = s.myPow(2.0, -2)
    print(r)
    r = s.myPow(2.0, -2147483648)
    print(r)
