class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l < r:
            m = (l + r) // 2
            if m ** 2 == num:
                return True
            elif m ** 2 < num:
                l = m + 1
            else:
                r = m
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.isPerfectSquare(16)
    print(r)
    r = s.isPerfectSquare(65536)
    print(r)
