class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target = sum(nums)
        if target % k != 0:
            return False
        target //= k

        nums.sort()
        if nums[-1] > target:
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        def helper(n, residues):
            if n == len(nums):
                return True
            for i, residue in enumerate(residues):
                if residue >= nums[n]:
                    residues[i] -= nums[n]
                    if helper(n + 1, residues):
                        return True
                    residues[i] += nums[n]
                elif residue == target:
                    break
            return False

        return helper(0, [target] * k)

    def canPartitionKSubsets2(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    r = s.canPartitionKSubsets2(nums, 4)
    print r
    nums = [10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6]
    r = s.canPartitionKSubsets2(nums, 3)
    print r
    nums = [2, 2, 2, 2, 3, 4, 5]
    r = s.canPartitionKSubsets2(nums, 4)
    print r
