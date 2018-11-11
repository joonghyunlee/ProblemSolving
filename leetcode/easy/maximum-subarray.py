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


if __name__ == '__main__':
    s = Solution()
    r = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print r
    r = s.maxSubArray([1])
    print r
    r = s.maxSubArray([-2, 1])
    print r
