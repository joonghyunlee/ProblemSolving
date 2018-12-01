class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.subs = []
        s = 0
        for i, n in enumerate(nums):
            s += n
            self.subs.append(s)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.subs[j]
        else:
            return self.subs[j] - self.subs[i - 1]


if __name__ == '__main__':
    s = NumArray([-2, 0, 3, -5, 2, -1])
    r = s.sumRange(0, 2)
    print r
    r = s.sumRange(2, 5)
    print r
    r = s.sumRange(0, 5)
    print r
