class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((s+[n] for s in dp if not s or n % s[-1] == 0), key=len))
        return max(dp, key=len)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print s.largestDivisibleSubset(nums)