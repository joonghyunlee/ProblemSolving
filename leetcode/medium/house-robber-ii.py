# case: n is even
# 1 2 3 1
# (1 + 3), (2 + 1)
# case: n is odd
# 1 2 3 1 5
# (1 + 3), (2 + 1), (5 + 3)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(subs):
            n = len(subs)
            if n == 1:
                return subs[0]

            memos = []
            for i in range(n):
                if i == 0 or i == 1:
                    memos.append(subs[i])
                    continue
                memos.append(max(memos[:i-1]) + subs[i])

            return max(memos)

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[:-1]), helper(nums[1:]))


if __name__ == '__main__':
    s = Solution()
    r = s.rob([1, 2, 3, 1, 5])
    print r
    r = s.rob([0])
    print r
    r = s.rob([1, 3, 1, 3, 100])
    print r
    r = s.rob([0, 0])
    print r
