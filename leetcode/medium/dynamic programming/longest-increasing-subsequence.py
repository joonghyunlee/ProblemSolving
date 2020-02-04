class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0:
            return 0
        m = [1] * n
        longest = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    m[i] = max(m[i], m[j] + 1)
            longest = max(longest, m[i])

        return longest


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 3, 101, 18]
    r = s.lengthOfLIS(nums)
    print(r)
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    r = s.lengthOfLIS(nums)
    print(r)
    nums = []
    r = s.lengthOfLIS(nums)
    print(r)
