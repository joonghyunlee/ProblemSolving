class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        memo = {}

        def helper(i, S):
            if i >= n:
                return 1 if S == 0 else 0
            if (i, S) in memo:
                return memo[(i, S)]
            memo[(i, S)] = helper(i+1, S-nums[i]) + helper(i+1, S+nums[i])
            return memo[(i, S)]
        return helper(0, S)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    r = s.findTargetSumWays(nums, 3)
    print(r)
