class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for n in nums:
            ret = ret ^ n

        return ret


if __name__ == '__main__':
    s = Solution()
    r = s.singleNumber([2, 2, 1])
    print r
    r = s.singleNumber([4, 1, 2, 1, 2])
    print r
