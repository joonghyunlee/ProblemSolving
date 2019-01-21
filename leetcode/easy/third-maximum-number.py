class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [None, None, None]
        for n in nums:
            if not m[0] or m[0] < n:
                m.insert(0, n)
                m.pop()
            elif m[0] == n:
                continue
            elif not m[1] or m[1] < n:
                m.insert(1, n)
                m.pop()
            elif m[1] == n:
                continue
            elif not m[2] or m[2] < n:
                m.insert(2, n)
                m.pop()
            print m
        return m[2] if m[2] or m[2] == 0  else m[0]


if __name__ == '__main__':
    s = Solution()
    r = s.thirdMax([3, 2, 1])
    print(r)
    r = s.thirdMax([2, 1])
    print(r)
    r = s.thirdMax([2, 2, 3, 1])
    print(r)
    r = s.thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3])
    print(r)
