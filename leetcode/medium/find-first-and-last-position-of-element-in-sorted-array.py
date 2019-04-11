class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        ret = []
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        else:
            ret.append(l)

        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        ret.append(r - 1)

        return ret


if __name__ == '__main__':
    s = Solution()
    nums = [3, 5, 7, 7, 8, 8, 10]
    r = s.searchRange(nums, 8)
    print r
    r = s.searchRange(nums, 6)
    print r
    r = s.searchRange([], 0)
    print r

    import random
    for time in range(10):
        nums = [random.randrange(1, 51) for i in range(20)]
        nums.sort()
        print nums
        target = random.randrange(1, 51)
        print target
        r = s.searchRange(nums, target)
        print r

