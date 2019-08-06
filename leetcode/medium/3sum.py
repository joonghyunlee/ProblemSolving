class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sums = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                l, r, m = i + 1, n - 1, 0 - nums[i]
                while l < r:
                    if nums[l] + nums[r] == m:
                        sums.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < m:
                        l += 1
                    else:
                        r -= 1
        return sums


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1, 0, 1, 2, -1, -4])
    print r
