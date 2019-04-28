class Solution:
    def findMagicIndex1(self, nums):
        for i, n in enumerate(nums):
            if i == n:
                return i
        return -1

    def findMagicIndex2(self, nums):
        def helper(l, r):
            m = (l + r) // 2
            if m == nums[m]:
                return m
            elif m > nums[m]:
                return helper(l, m)
            else:
                return helper(m + 1, r)
        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 6]
    r = s.findMagicIndex1(nums)
    print r
    r = s.findMagicIndex2(nums)
    print r
