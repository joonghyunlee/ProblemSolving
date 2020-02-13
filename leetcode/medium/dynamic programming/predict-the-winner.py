class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = [[None] * n for _ in range(n)]

        def helper(l, r):
            if memo[l][r]:
                return memo[l][r]
            elif l == r:
                return nums[l]
            memo[l][r] = max(nums[l] - helper(l + 1, r),
                             nums[r] - helper(l, r - 1))
            return memo[l][r]
        return True if helper(0, len(nums) - 1) >= 0 else False

    def PredictTheWinner2(self, nums):
        n = len(nums)
        memo = [[None] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            memo[l][l] = nums[l]
            for r in range(l + 1, n):
                memo[l][r] = max(nums[l] - memo[l + 1][r],
                                 nums[r] - memo[l][r - 1])
        return memo[0][n - 1] >= 0

    def PredictTheWinner3(self, nums):
        n = len(nums)
        memo = [0] * n
        for l in range(n - 1, -1, -1):
            memo[l] = nums[l]
            for r in range(l + 1, n):
                memo[r] = max(nums[l] - memo[r],
                              nums[r] - memo[l - 1])
        return memo[n - 1] >= 0


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 2]
    print s.PredictTheWinner(nums)
    print s.PredictTheWinner2(nums)
    print s.PredictTheWinner3(nums)
    nums = [1, 5, 233, 7]
    print s.PredictTheWinner(nums)
    print s.PredictTheWinner2(nums)
    print s.PredictTheWinner3(nums)
    nums = [3, 5, 3]
    print s.PredictTheWinner(nums)
    print s.PredictTheWinner2(nums)
    print s.PredictTheWinner3(nums)
