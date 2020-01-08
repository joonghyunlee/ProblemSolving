class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        pl, pr = [0] * n, [0] * n
        ans = []
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]

        # left
        tot = sums[k] - sums[0]
        for i in range(k, n):
            if sums[i + 1] - sums[i + 1 - k] > tot:
                pl[i] = i + 1 - k
                tot = sums[i + 1] - sums[i + 1 - k]
            else:
                pl[i] = pl[i - 1]

        # right
        pr[n - k] = n - k
        tot = sums[n] - sums[n - k]
        for i in range(n - k - 1, -1, -1):
            if sums[i + k] - sums[i] >= tot:
                pr[i] = i
                tot = sums[i + k] - sums[i]
            else:
                pr[i] = pr[i + 1]

        # mid
        ms = 0
        for i in range(k, n - 2 * k):
            l = pl[i - 1]
            r = pr[i + k]
            tot = (sums[i + k] - sums[i]) + \
                (sums[l + k] - sums[l]) + (sums[r + k] - sums[r])
            if tot > ms:
                ms = tot
                ans = [l, i, r]

        return ans

    def maxSumOfThreeSubarrays2(self, nums, k):
        n = len(nums)
        p1 = 0
        p2 = [0, k]
        p3 = [0, k, k * 2]

        s1 = sum(nums[0:k])
        s2 = sum(nums[k:k * 2])
        s3 = sum(nums[k * 2:k * 3])

        m1 = s1
        m2 = s1 + s2
        m3 = s1 + s2 + s3

        i1 = 1
        i2 = k + 1
        i3 = k * 2 + 1
        while i3 <= n - k:
            s1 = s1 - nums[i1 - 1] + nums[i1 + k - 1]
            s2 = s2 - nums[i2 - 1] + nums[i2 + k - 1]
            s3 = s3 - nums[i3 - 1] + nums[i3 + k - 1]

            # First sequence
            if s1 > m1:
                p1 = i1
                m1 = s1

            # Second sequence
            if s2 + m1 > m2:
                p2 = [p1, i2]
                m2 = s2 + m1

            # Third sequence
            if s3 + m2 > m3:
                p3 = p2 + [i3]
                m3 = s3 + m2

            i1 += 1
            i2 += 1
            i3 += 1

        return p3


if __name__ == '__main__':
    s = Solution()
    r = s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
    print r
    r = s.maxSumOfThreeSubarrays2([1, 2, 1, 2, 6, 7, 5, 1], 2)
    print r
    r = s.maxSumOfThreeSubarrays2([4, 5, 10, 6, 11, 17, 4, 11, 1, 3], 1)
    print r
