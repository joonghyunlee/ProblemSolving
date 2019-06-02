class Solution(object):
    def find132pattern(self, nums):
        for i, n in enumerate(nums):
            bigs = []
            for j in range(i + 1, len(nums)):
                if nums[j] > n:
                    bigs.append(nums[j])
            for k in range(len(bigs) - 1):
                if bigs[k] > bigs[k+1]:
                    return True
        return False

    def find132pattern2(self, nums):
        import sys
        stack = []
        s3 = -sys.maxint
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.find132pattern([3, 1, 4, 2])
    print r
    r = s.find132pattern2([3, 1, 4, 2])
    print r
    r = s.find132pattern([-1, 3, 2, 0])
    print r
    r = s.find132pattern2([-1, 3, 2, 0])
    print r
    r = s.find132pattern([1, 0, 1, -4, 3])
    print r
    r = s.find132pattern2([1, 0, 1, -4, 3])
    print r
