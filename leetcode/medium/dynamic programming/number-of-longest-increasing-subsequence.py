class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        lengths = [0] * n   # the length of the LIS which ends with nums[i]
        counts = [0] * n    # the number of the LIS which ends with nums[i]
        # lengths[k + 1] = max(lengths[k + 1], lengths[i] + 1) for all i <= k and nums[i] < nums[k + 1]
        # counts[k + 1] = sum(counts[i]) for all i <= k and nums[i] < nums[k + 1] and lengths[i] = lengths[k + 1] - 1
        for j in range(n):
            lengths[j] = counts[j] = 1
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = lengths[i] + 1
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 4, 7]
    r = s.findNumberOfLIS(nums)
    print r
    nums = [5, 5, 5, 5, 5]
    r = s.findNumberOfLIS(nums)
    print r
    nums = [1, 2, 4, 3, 5, 4, 7, 2]
    r = s.findNumberOfLIS(nums)
    print r