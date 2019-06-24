class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:
                l += 1
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [2, 5, 6, 0, 0, 1, 2]
    r = s.search(nums, 0)
    print r
    nums = [2, 5, 6, 0, 0, 1, 2]
    r = s.search(nums, 3)
    print r
    nums = [2, 5, 6, 7, 0, 0, 1, 2]
    r = s.search(nums, 3)
    print r
    nums = [2, 5, 6, 7, 0, 0, 1, 2]
    r = s.search(nums, 1)
    print r
    nums = []
    r = s.search(nums, 5)
    print r
    nums = [3, 1]
    r = s.search(nums, 1)
    print r
    nums = [1, 3, 1, 1, 1]
    r = s.search(nums, 3)
    print r
