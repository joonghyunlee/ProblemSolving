class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2:
            return False
        memo = {}

        def helper(i, target):
            if target == 0:
                return True
            elif i >= len(nums):
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            ans = helper(i+1, target-nums[i]) or helper(i+1, target)
            memo[(i, target)] = ans
            return ans

        return helper(0, total // 2)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 11, 5]
    r = s.canPartition(nums)
    print(r)
    nums = [1, 2, 3, 5]
    r = s.canPartition(nums)
    print(r)
