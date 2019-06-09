class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        largest = 0
        memo = [[0] * n for i in range(m)]
        for i in range(m):
            if matrix[i][0] == '1':
                largest = 1
                memo[i][0] = 1
        for j in range(n):
            if matrix[0][j] == '1':
                largest = 1
                memo[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue

                w = memo[i - 1][j - 1]
                bottom, right = 0, 0
                for k in range(w + 1):
                    if matrix[i - k][j] == '0':
                        break
                    right += 1
                for k in range(w + 1):
                    if matrix[i][j - k] == '0':
                        break
                    bottom += 1

                memo[i][j] = min(bottom, right)
                largest = max(largest, memo[i][j] ** 2)

        return largest


if __name__ == '__main__':
    s = Solution()
    matrix = [
        ['1', '0', '1', '0', '0', '0', '1', '1', '0'],
        ['1', '0', '1', '1', '1', '1', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '1', '1'],
        ['0', '1', '1', '1', '1', '1', '0', '1', '0']
    ]
    r = s.maximalSquare(matrix)
    print r
    matrix = [
        ['1']
    ]
    r = s.maximalSquare(matrix)
    print r
    matrix = [
        ['0', '0', '0', '1'],
        ['1', '1', '0', '1'],
        ['1', '1', '1', '1'],
        ['0', '1', '1', '1'],
        ['0', '1', '1', '1']
    ]
    r = s.maximalSquare(matrix)
    print r
    print matrix
