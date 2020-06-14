class Solution:
    def splitArray(self, nums: 'List[int]', m: int) -> int:
        from functools import lru_cache
        @lru_cache()
        def helper(l, n, k):
            if (n - l) <= k:
                return max(nums[l:n])
            if k == 1:
                return sum(nums[l:n])
            largest = float("inf")
            for i in range(l + 1, n - k + 2):
                new = max(sum(nums[l:i]), helper(i, n, k - 1))
                largest = min(largest, new)
            return largest
        return helper(0, len(nums), m)

    def splitArray2(self, nums: 'List[int]', m: int) -> int:
        def helper(i, m):
            if i == len(nums):
                return 0
            elif m == 1:
                return sum(nums[i:])
            else:
                if i in cache and m in cache[i]:
                    return cache[i][m]
                cache[i][m] = float('inf')
                for j in range(1, len(nums)+1):
                    left, right = sum(
                        nums[i:i+j]), helper(i+j, m-1)
                    cache[i][m] = min(cache[i][m], max(left, right))
                    if left > right:
                        break
                return cache[i][m]

        from collections import defaultdict 
        cache = defaultdict(dict)
        return helper(0, m)


if __name__ == '__main__':
    s = Solution()
    nums = [7, 2, 5, 10, 8]
    r = s.splitArray(nums, 2)
    print(r)
    r = s.splitArray2(nums, 2)
    print(r)
