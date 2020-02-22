class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        points = [0] * (max(nums) + 1)
        for num in nums:
            points[num] += num

        prev, curr = 0, 0
        for point in points:
            prev, curr = curr, max(prev + point, curr)
        return curr


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4, 2]
    r = s.deleteAndEarn(nums)
    print r
    nums = [2, 2, 3, 3, 3, 4]
    r = s.deleteAndEarn(nums)
    print r