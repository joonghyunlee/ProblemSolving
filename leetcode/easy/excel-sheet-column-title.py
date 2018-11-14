class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = 26
        power = 1

        nums = [n % s]
        while n >= (s ** power):
            print "s ** power:", s ** power
            print "digit:", n % (s ** power)
            nums.append(n % (s ** power))
            power += 1

        nums.reverse()
        print nums
        print ''.join([chr(x + ord('A')) for x in nums])


if __name__ == '__main__':
    s = Solution()
    s.convertToTitle(1)
    s.convertToTitle(28)
    s.convertToTitle(701)
