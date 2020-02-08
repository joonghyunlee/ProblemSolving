class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 2:
            return 1 if nums[0] == nums[1] else 2
        elif n < 2:
            return n

        memo = [[0] * n, [0] * n]
        memo[0][1] = 2 if nums[0] > nums[1] else 1
        memo[1][1] = 2 if nums[0] < nums[1] else 1
        for i in range(2, n):
            memo[0][i], memo[1][i] = 1, 1
            for j in range(0, i):
                if nums[j] > nums[i]:
                    memo[0][i] = max(memo[0][i], memo[1][j] + 1)
                elif nums[j] < nums[i]:
                    memo[1][i] = max(memo[1][i], memo[0][j] + 1)
        return max(memo[0][-1], memo[1][-1])


if __name__ == '__main__':
    s = Solution()
    nums = [1, 7, 4, 9, 2, 5]
    print s.wiggleMaxLength(nums)
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    print s.wiggleMaxLength(nums)
    nums = [17, 5, 10, 13, 15, 10, 5, 16, 8]
    print s.wiggleMaxLength(nums)
    nums = [0, 0, 0]
    print s.wiggleMaxLength(nums)
