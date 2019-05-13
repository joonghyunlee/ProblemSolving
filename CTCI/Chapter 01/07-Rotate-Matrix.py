class Solution:
    def rotate(self, m):
        n = len(m)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                tl = m[i][j]
                tr = m[j][n - 1 - i]
                br = m[n - 1 - i][n - 1 - j]
                bl = m[n - 1 - j][i]

                m[i][j] = bl
                m[j][n - 1 - i] = tl
                m[n - 1 - i][n - 1 - j] = tr
                m[n - 1 - j][i] = br


if __name__ == '__main__':
    s = Solution()
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    s.rotate(m)
    print m
