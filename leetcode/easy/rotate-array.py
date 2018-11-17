class Solution(object):
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())

    def rotate2(self, nums, k):
        def rotateOne(nums):
            d = nums[0]
            for i in range(1, len(nums)):
                nums[i], d = d, nums[i]
            nums[0] = d
        for i in range(k):
            rotateOne(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate2(nums, 3)
    print nums
    nums = [-1, -100, 3, 99]
    s.rotate2(nums, 2)
    print nums
