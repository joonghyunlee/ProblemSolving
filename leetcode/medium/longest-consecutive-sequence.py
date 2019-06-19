class Solution(object):
    def longestConsecutive(self, nums):
        cov = {}
        for n in nums:
            ll, lr = cov.get(n - 1, (None, None))
            rl, rr = cov.get(n + 1, (None, None))

            cov[n] = (
                ll if ll is not None else n,
                rr if rr is not None else n
            )

            if ll is not None:
                cov[n - 1] = (ll, cov[n][1])

            if rr is not None:
                cov[n + 1] = (cov[n][0], rr)

        ml = 0
        for n in nums:
            if n not in cov:
                continue

            l, r = cov.pop(n)

            while l != n and l in cov:
                ll, lr = cov.pop(l)
                l = min(l, ll)
                r = max(r, lr)

            while r != n and r in cov:
                rl, rr = cov.pop(r)
                l = min(l, rl)
                r = max(r, rr)

            ml = max(ml, abs(r - l + 1))

        return ml


if __name__ == '__main__':
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    r = s.longestConsecutive(nums)
    print(r)
    nums = []
    r = s.longestConsecutive(nums)
    print(r)
    nums = [1, 2, 0, 1]
    r = s.longestConsecutive(nums)
    print(r)
    nums = [0, 0, 1 - 1]
    r = s.longestConsecutive(nums)
    print(r)
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    r = s.longestConsecutive(nums)
    print(r)
    nums = [5, -7, -8, 7, 6, 5, -8, 9, 4, 4, 2, 0, -2, 6,
            6, 2, 6, 7, -5, 5, -8, -3, -2, 4, -4, -1, 5, 9, -8]
    r = s.longestConsecutive(nums)
    print(r)
