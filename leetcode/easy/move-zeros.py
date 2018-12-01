class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        d = 0
        for i, n in enumerate(nums):
            if n:
                nums[i], nums[d] = 0, n
                d += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print nums
    nums = [1]
    s.moveZeroes(nums)
    print nums
