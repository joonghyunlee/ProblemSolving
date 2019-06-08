class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ms = []
        for i in range(len(nums)):
            m, rm = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                rm *= nums[j]
                m = max(m, rm)
            ms.append(m)
        return max(ms)

    def maxProduct2(self, nums):
        m, rm, rn = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            rm, rn = max(rm * n, rn * n, n), min(rn * n, rm * n, n)
            m = max(m, rm, rn)
        return m


if __name__ == '__main__':
    s = Solution()
    r = s.maxProduct2([2, 3, -2, 4])
    print r
    r = s.maxProduct2([-2, 0, -1])
    print r
    r = s.maxProduct2([-2, 3, -4])
    print r
    r = s.maxProduct2([0, 2])
    print r
    r = s.maxProduct2([-1, -2, -9, -6])
    print r
    r = s.maxProduct2([2, -5, -2, -4, 3])
    print r
