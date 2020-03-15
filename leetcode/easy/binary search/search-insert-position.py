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

    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
        if nums[l] < target:
            return l + 1
        return l


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 6]
    r = s.searchInsert(nums, 5)
    print r
    r = s.searchInsert2(nums, 5)
    print r
    r = s.searchInsert(nums, 2)
    print r
    r = s.searchInsert2(nums, 2)
    print r
    r = s.searchInsert(nums, 7)
    print r
    r = s.searchInsert2(nums, 7)
    print r
    r = s.searchInsert(nums, 0)
    print r
    r = s.searchInsert2(nums, 0)
    print r