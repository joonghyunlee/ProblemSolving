class Solution:
    def pancakeSort(self, A: 'List[int]') -> 'List[int]':
        res = []
        n = len(A)
        for i in range(n, 1, -1):
            mv = max(A[:i])
            mi = A.index(mv)
            res.append(mi + 1)
            for j in range((mi + 1) // 2):
                A[j], A[mi - j] = A[mi - j], A[j]

            res.append(i)
            for j in range(i // 2):
                A[j], A[i - 1 - j] = A[i - 1 - j], A[j]

        return res


if __name__ == '__main__':
    s = Solution()
    A = [3, 2, 4, 1]
    r = s.pancakeSort(A)
    print(r)
