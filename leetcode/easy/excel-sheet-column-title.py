class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = 26
        nums = []
        while n > 0:
            if n % s == 0:
                nums.append(s - 1)
                n -= s
            else:
                nums.append(n % s - 1)

            n //= s

        nums.reverse()
        return ''.join([chr(x + ord('A')) for x in nums])


if __name__ == '__main__':
    s = Solution()
    r = s.convertToTitle(1)
    print r
    r = s.convertToTitle(28)
    print r
    r = s.convertToTitle(701)
    print r
    r = s.convertToTitle(26)
    print r
