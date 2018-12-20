class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return (a ^ b) & (a & b)


if __name__ == '__main__':
    s = Solution()
    r = s.getSum(1, 2)
    print r
    r = s.getSum(-2, 3)
    print r
