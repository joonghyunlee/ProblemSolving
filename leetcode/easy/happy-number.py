class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digitSquareSum(m):
            ss = 0
            while m > 0:
                ss += (m % 10) ** 2
                m //= 10
            return ss

        history = set()
        s = n
        while s > 0:
            s = digitSquareSum(s)
            if s == 1:
                return True
            if s in history:
                return False
            history.add(s)
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.isHappy(9133)
    print r
    r = s.isHappy(19)
    print r
