class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n, m = len(A), len(B)
        memo = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    memo[i + 1][j + 1] = memo[i][j] + 1
        return max(max(row) for row in memo)


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    r = s.findLength(A, B)
    print r
