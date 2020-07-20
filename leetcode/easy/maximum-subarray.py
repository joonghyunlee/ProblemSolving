class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        r_sum = nums[0]
        for n in nums[1:]:
            r_sum = max(r_sum + n, n)
            max_sum = max(max_sum, r_sum)

        return max_sum

    def maxSubArray2(self, nums: 'List[int]') -> int:
        ss, ls = nums[0], nums[0]
        for num in nums[1:]:
            ls = max(ls + num, num)
            ss = max(ss, ls)
        return ss

    def maxSubArray3(self, nums: 'List[int]') -> int:
        def helper(l, r):
            if l == r:
                return nums[l], nums[l], nums[l], nums[l]
            elif l > r:
                return 0, 0, 0, 0
            m = (l + r) // 2
            lms, lls, lrs, las = helper(l, m)
            rms, rls, rrs, ras = helper(m + 1, r)
            
            ms = max(lms, rms, lrs + rls)
            ls = max(las, las + rls, lls)
            rs = max(ras, ras + lrs, rrs)
            als = las + ras
            return ms, ls, rs, als
            
        n = len(nums)
        if n == 0:
            return 0
        ms, _, _, _ = helper(0, n - 1)
        return ms


if __name__ == '__main__':
    s = Solution()
    r = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(r)
    r = s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(r)
    r = s.maxSubArray3([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(r)
    r = s.maxSubArray([1])
    print(r)
    r = s.maxSubArray2([1])
    print(r)
    r = s.maxSubArray3([1])
    print(r)
    r = s.maxSubArray([-2, 1])
    print(r)
    r = s.maxSubArray2([-2, 1])
    print(r)
    r = s.maxSubArray3([-2, 1])
    print(r)
