import random


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    print("[%d, %d]" % (i, j))
                    return i, j


if __name__ == "__main__":
    s = Solution()

    nums = [random.randrange(-100, 101) for _ in range(100)]
    a = nums[random.randrange(0, 101)]
    print a
    b = nums[random.randrange(0, 101)]
    print b
    target = a + b

    for i in range(0, 10):
        for j in range(0, 10):
            print "nums[%d] = %d " % (i*10 + j, nums[i*10 + j]),
        print
    print target

    s.twoSum(nums, target)
