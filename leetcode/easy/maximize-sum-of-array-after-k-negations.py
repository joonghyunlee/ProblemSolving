class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        m = None
        for i, n in enumerate(A):
            if n < 0 and K > 0:
                A[i] = -n
                K -= 1
            if m is None or A[i] < m:
                m = A[i]
        if K <= 0 or K % 2 == 0:
            return sum(A)
        return sum(A) - 2 * m


if __name__ == '__main__':
    s = Solution()
    A = [2, -3, -1, 5, -4]
    r = s.largestSumAfterKNegations(A, 2)
    print(r)
    A = [3, -1, 0, 2]
    r = s.largestSumAfterKNegations(A, 3)
    print(r)
    A = [4, 2, 3]
    r = s.largestSumAfterKNegations(A, 1)
    print(r)
