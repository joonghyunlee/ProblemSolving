class Solution(object):
    def rob(self, nums):
        s = []
        for i in range(len(nums)):
            if i == 0 or i == 1:
                s.append(nums[i])
                continue
            c = max(s[:i-1]) + nums[i]
            s.append(c)

        return max(s)


if __name__ == '__main__':
    s = Solution()
    r = s.rob([0, 1, 3, 5, 8, 0, 1, 7, 6, 2])
    print r
    r = s.rob([1, 2, 3, 1])
    print r
    r = s.rob([2, 7, 9, 3, 1])
    print r
