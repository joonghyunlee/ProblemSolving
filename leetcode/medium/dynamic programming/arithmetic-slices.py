class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        cnt = 0
        for i in range(0, n - 2):
            diff = A[i + 1] - A[i]
            for j in range(i + 2, n):
                if A[j] - A[j - 1] == diff:
                    cnt += 1
                else:
                    break
        return cnt

    def numberOfArithmeticSlices2(self, A):
        n = len(A)
        total = [0]
        def slices(A, i):
            if i < 2:
                return 0
            ap = 0
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                ap = 1 + slices(A, i - 1)
                total[0] += ap
            else:
                slices(A, i - 1)
            return ap
        slices(A, n - 1)
        return total

    def numberOfArithmeticSlices3(self, A):
        n = len(A)
        memo = [0] * n
        total = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                memo[i] = 1 + memo[i - 1]
                total += memo[i]
        return total


if __name__ == '__main__':
    s = Solution()
    A = [1, 3, 5, 7, 9]
    print s.numberOfArithmeticSlices3(A)
