class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys

        def helper(l, r):
            m = (l + r) // 2
            lv = nums[m - 1] if m > 0 else -sys.maxsize
            rv = nums[m + 1] if m < len(nums) - 1 else -sys.maxsize
            if lv < nums[m] and rv < nums[m]:
                return m
            elif lv < nums[m] and rv > nums[m]:
                l = m + 1
            else:
                r = m
            return helper(l, r)

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 1]
    r = s.findPeakElement(nums)
    print r
    nums = [1, 2, 1, 3, 5, 6, 4]
    r = s.findPeakElement(nums)
    print r
    nums = [1, 2]
    r = s.findPeakElement(nums)
    print r
    nums = [3, 2, 1]
    r = s.findPeakElement(nums)
    print r
