class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def helper(l, r):
            m = (l + r) // 2
            if A[m - 1] < A[m] and A[m] > A[m + 1]:
                return m
            elif A[m - 1] < A[m] and A[m] < A[m + 1]:
                l = m + 1
            else:
                r = m
            return helper(l, r)
        return helper(0, len(A) - 1)


if __name__ == '__main__':
    s = Solution()
    A = [0, 1, 0]
    r = s.peakIndexInMountainArray(A)
    print r
    A = [0, 2, 1, 0]
    r = s.peakIndexInMountainArray(A)
    print r
    A = [1, 3, 2]
    r = s.peakIndexInMountainArray(A)
    print r
    A = [3, 4, 5, 1]
    r = s.peakIndexInMountainArray(A)
    print r
