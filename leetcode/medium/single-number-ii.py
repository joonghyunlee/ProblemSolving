class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        a b c
        0 0 0 0 0
        0 1 0 0 1
        1 0 0 1 0
        0 0 1 0 1
        0 1 1 1 0
        1 0 1 0 0
        """
        a, b = 0, 0
        for n in nums:
            ta = a & ~b & ~n | ~a & b & n
            b = ~a & b & ~n | ~a & ~b & n
            a = ta

        return a | b


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3, 2]
    r = s.singleNumber(nums)
    print(r)
