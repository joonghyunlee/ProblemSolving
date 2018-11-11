class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] > target or nums[i] == target:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    r = s.searchInsert([1, 3, 5, 6], 5)
    print r
    r = s.searchInsert([1, 3, 5, 6], 2)
    print r
    r = s.searchInsert([1, 3, 5, 6], 7)
    print r
    r = s.searchInsert([1, 3, 5, 6], 0)
    print r
