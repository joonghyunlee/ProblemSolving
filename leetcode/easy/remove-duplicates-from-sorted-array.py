class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        duplicate = nums[0]
        count = 0
        for i in range(len(nums)):
            if duplicate == nums[i]:
                count = count + 1
            else:
                duplicate = nums[i]
                nums[i-count+1] = duplicate

        return len(nums) - count + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    r = s.removeDuplicates(nums)
    print r

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    r = s.removeDuplicates(nums)
    print r
