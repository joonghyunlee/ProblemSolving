class Solution:
    def subarraysDivByK(self, A: 'List[int]', K: int) -> int:
        n = len(A)
        sums = [[0] * (n + 1) for _ in range(n)]
        answer = 0
        for left in range(n):
            for right in range(left + 1, n + 1):
                sums[left][right] = sums[left][right - 1] + A[right - 1]
                if sums[left][right] % K == 0:
                    answer += 1
        return answer

    # let N = len(A), then there are N prefix sum.
    # To calculate how many subarrays are divisible by K is logically
    # equivalent to how many ways can we pair up all prefix sum pairs (i, j)
    # where i < j such that (prefix[j] - prefix_sum[i]) % K == 0.
    # And it is true iff prefix[j] % K == prefix[i] % K
    def subarraysDivByK2(self, A: 'List[int]', K: int) -> int:
        n = len(A)
        modGroups = [0] * K
        preSum = 0
        for i in range(n):
            preSum += A[i]
            residueGroup = preSum % K
            if residueGroup < 0:
                residueGroup += K
            modGroups[residueGroup] += 1

        answer = 0
        for x in modGroups:
            # calculate all computations for each mod groups
            if x > 1:
                answer += (x * (x - 1)) // 2

        return answer + modGroups[0]



if __name__ == '__main__':
    s = Solution()
    A = [4, 5, 0, -2, -3, 1]
    r = s.subarraysDivByK(A, 5)
    print(r)
    r = s.subarraysDivByK2(A, 5)
    print(r)
