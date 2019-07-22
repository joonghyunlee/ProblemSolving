class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(n // 2 + 1):
            for j in range(i, n - i):
                lt, rt = matrix[i][j], matrix[j][n - i]
                rb, lb = matrix[n - i][n - j], matrix[n - j][i]
                matrix[i][j] = lb
                matrix[j][n - i] = lt
                matrix[n - i][n - j] = rt
                matrix[n - j][i] = rb


if __name__ == '__main__':
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    for i in range(len(matrix)):
        print(matrix[i])
    s = Solution()
    s.rotate(matrix)
    for i in range(len(matrix)):
        print(matrix[i])
