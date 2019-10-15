class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])

        states = [[0] * m for _ in range(n)]

        def dfs(x, y):
            if states[y][x] > 0:
                return states[y][x]

            states[y][x] = -1
            max_len = 1
            path = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dx, dy in path:
                if x + dx < 0 or x + dx >= m:
                    continue
                if y + dy < 0 or y + dy >= n:
                    continue
                if matrix[y][x] >= matrix[y + dy][x + dx]:
                    continue
                if states[y + dy][x + dx] < 0:
                    continue

                l = dfs(x + dx, y + dy)
                max_len = max(max_len, l + 1)

            states[y][x] = max_len
            return max_len

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return max(map(max, states))


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    r = s.longestIncreasingPath(matrix)
    print r
    matrix = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    r = s.longestIncreasingPath(matrix)
    print r
    matrix = [
        [2, 1]
    ]
    r = s.longestIncreasingPath(matrix)
    print r
