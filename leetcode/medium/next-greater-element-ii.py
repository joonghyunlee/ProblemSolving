class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1]
    r = s.nextGreaterElements(nums)
    print r
    nums = [1, 2, 3, 2, 1]
    r = s.nextGreaterElements(nums)
    print r
