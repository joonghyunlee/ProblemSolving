class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        tail = len(nums) - 1
        head = 0
        while head <= tail:
            if nums[head] == val and nums[tail] == val:
                tail = tail - 1
            elif nums[head] == val and nums[tail] != val:
                nums[head] = nums[tail]
                nums[tail] = val
                tail = tail - 1
                head = head + 1
            elif nums[head] != val and nums[tail] == val:
                tail = tail - 1
                head = head + 1
            elif nums[head] != val and nums[tail] != val:
                head = head + 1

        return head


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    r = s.removeElement(nums, 2)
    print r
    for i in range(r):
        print "%d" % nums[i],
    print
