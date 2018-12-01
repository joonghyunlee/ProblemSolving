class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [0,3,5,1,2,6,9,4,7]
    r = s.missingNumber(nums)
    print(r)
