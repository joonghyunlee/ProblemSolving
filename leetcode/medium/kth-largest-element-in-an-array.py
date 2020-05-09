class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        import heapq
        conv = [-num for num in nums]
        heapq.heapify(conv)

        smallest = 0
        while k > 0:
            smallest = heapq.heappop(conv)
            k -= 1

        return -smallest

    def findKthLargest2(self, nums: 'List[int]', k: int) -> int:
        def partition(nums: 'List[int]', lo: int, hi: int) -> int:
            i, j = lo, hi + 1
            while 1:
                while 1:
                    i += 1
                    if not (i < hi and nums[i] < nums[lo]):
                        break
                while 1:
                    j -= 1
                    if not (j > lo and nums[lo] < nums[j]):
                        break
                if i >= j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            nums[lo], nums[j] = nums[j], nums[lo]
            return j

        n = len(nums)
        k = n - k
        lo, hi = 0, n - 1
        while lo < hi:
            j = partition(nums, lo, hi)
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                break

        return nums[k]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    r = s.findKthLargest(nums, 2)
    print(r)
    nums = [3, 2, 1, 5, 6, 4]
    r = s.findKthLargest2(nums, 2)
    print(r)
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    r = s.findKthLargest(nums, 4)
    print(r)
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    r = s.findKthLargest2(nums, 4)
    print(r)
    nums = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    r = s.findKthLargest2(nums, 1)
    print(r)
