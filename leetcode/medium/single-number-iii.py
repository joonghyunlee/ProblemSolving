class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for n in nums:
            x ^= n

        x = x & ~(x - 1)

        a, b = 0, 0
        for n in nums:
            if n & x:
                a ^= n
            else:
                b ^= n

        return [a, b]


if __name__ == '__main__':
    s = Solution()
    r = s.singleNumber([1, 2, 1, 3, 2, 5])
    print r
