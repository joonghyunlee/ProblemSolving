class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        c = 0
        t = nums[0]
        for num in nums:
            if num == t:
                c += 1
            else:
                c = 1
                t = num

            if c == (len(nums) // 2) + 1:
                return t


if __name__ == '__main__':
    s = Solution()
    r = s.majorityElement([3, 2, 3])
    print r
    r = s.majorityElement([2, 2, 1, 1, 1, 2, 2])
    print r
    r = s.majorityElement([2])
    print r
