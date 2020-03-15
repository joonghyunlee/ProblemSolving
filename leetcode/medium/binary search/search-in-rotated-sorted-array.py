class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target <= nums[r]:
                l = m + 1
            elif nums[l] <= target < nums[m]:
                r = m
            elif (nums[m] < nums[l] <= target) or \
                    (target < nums[m] < nums[l]):
                r = m
            else:
                l = m + 1
        return l if nums[l] == target else -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    r = s.search(nums, 0)
    print r
    r = s.search2(nums, 0)
    print r

    nums = [4, 5, 6, 7, 0, 1, 2]
    r = s.search(nums, 3)
    print r
    r = s.search2(nums, 3)
    print r

    nums = [3, 1]
    r = s.search(nums, 1)
    print r
    r = s.search2(nums, 1)
    print r

    nums = [5, 1, 3]
    r = s.search(nums, 5)
    print r
    r = s.search2(nums, 5)
    print r