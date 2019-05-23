class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resp = []
        l = 2 ** len(nums)
        for i in range(l):
            sub = []
            for j in range(len(nums)):
                if i & (1 << j):
                    sub.append(nums[j])
            resp.append(sub)
        return resp


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    r = s.subsets(nums)
    print(r)
