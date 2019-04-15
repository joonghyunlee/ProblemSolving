class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        mask = 0b1
        h = 0
        while z >= mask:
            h += 1 if z & mask else 0
            mask <<= 1
        return h


if __name__ == '__main__':
    s = Solution()
    r = s.hammingDistance(4, 1)
    print(r)
