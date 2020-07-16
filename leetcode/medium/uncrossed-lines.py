class Solution:
    def maxUncrossedLines(self, A: 'List[int]', B: 'List[int]') -> int:
        nA, nB = len(A), len(B)
        lines = [[0] * (nB + 1) for _ in range(nA + 1)]
        for i in range(nA):
            for j in range(nB):
                lines[i + 1][j + 1] = max(lines[i + 1][j], lines[i][j + 1])
                if A[i] == B[j]:
                    lines[i + 1][j + 1] = max(lines[i + 1][j + 1],
                                              lines[i][j] + 1)
        return lines[nA][nB]


if __name__ == '__main__':
    s = Solution()
    A = [1, 4, 2]
    B = [1, 2, 4]
    r = s.maxUncrossedLines(A, B)
    print(r)