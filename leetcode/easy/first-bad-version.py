# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    global errors
    return errors[version - 1] == 1

def generateTestSet(n):
    import random
    s = random.randrange(1, n)
    print "s:", s
    return [1 if i > s else 0
            for i in range(n)]

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l

    def firstBadVersion2(self, n):
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i


if __name__ == '__main__':
    s = Solution()
    for _ in range(5):
        errors = generateTestSet(10)
        print(errors)
        r = s.firstBadVersion(10)
        print(r)
        r = s.firstBadVersion2(10)
        print(r)
