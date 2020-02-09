class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = [None] * (target + 1)
        memo[0] = 1

        def helper(nums, target):
            if target < 0:
                return 0

            if memo[target] is not None:
                return memo[target]

            total = 0
            for num in nums:
                total += helper(nums, target - num)

            memo[target] = total

            return total

        return helper(nums, target)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print s.combinationSum4(nums, 4)
    nums = [4, 2, 1]
    print s.combinationSum4(nums, 32)
