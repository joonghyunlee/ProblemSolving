class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 0b1
        while num >= mask:
            mask <<= 1
        mask -= 1
        return mask ^ num


if __name__ == '__main__':
    s = Solution()
    r = s.findComplement(5)
    print(r)
    r = s.findComplement(1)
    print(r)
