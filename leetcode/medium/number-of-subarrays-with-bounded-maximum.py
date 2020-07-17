class Solution(object):
    def numSubarrayBoundedMax(self, A: 'List[int]', L: int, R: int) -> int:
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        n = len(A)
        cnt = len(list(filter(lambda x: L <= x <= R, A)))
        for i in range(n):
            subMax = A[i]
            for j in range(i + 1, n):
                subMax = max(subMax, A[j])
                cnt += 1 if L <= subMax <= R else 0
        return cnt

    def numSubarrayBoundedMax2(self, A: 'List[int]', L: int, R: int) -> int:
        n = len(A)
        cnt, dp = 0, 0
        prev = -1
        for i in range(n):
            if A[i] < L and i > 0:
                cnt += dp
            elif A[i] > R:
                dp = 0
                prev = i
            elif L <= A[i] <= R:
                dp = i - prev
                cnt += dp
        return cnt
        

if __name__ == '__main__':
    s = Solution()
    A = [2, 1, 4, 3]
    L, R = 2, 3
    print(s.numSubarrayBoundedMax(A, L, R))
