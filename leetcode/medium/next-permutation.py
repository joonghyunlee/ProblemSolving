class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def rever(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        i = len(nums) - 2
        while i >= 0 and (nums[i] >= nums[i + 1]):
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0:
                if nums[i] < nums[j]:
                    break
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
        rever(i + 1, len(nums) - 1)


if __name__ == '__main__':
    nums = [1, 3, 2]
    s = Solution()
    s.nextPermutation(nums)
    print nums
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    s.nextPermutation(nums)
    print nums
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    print nums
