class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        paths = []
        n = len(grid)
        m = len(grid[0])
        for j in range(n):
            row = []
            paths.append(row)
            for i in range(m):
                if i == 0 and j == 0:
                    row.append(grid[j][i])
                elif j == 0:
                    v = paths[j][i - 1] + grid[j][i]
                    row.append(v)
                elif i == 0:
                    v = paths[j - 1][i] + grid[j][i]
                    row.append(v)
                else:
                    v = min(paths[j - 1][i], paths[j][i - 1])
                    v += grid[j][i]
                    row.append(v)
        return paths[n - 1][m - 1]


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    r = s.minPathSum(grid)
    print(r)
