class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        paths = []
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for j in range(n):
            row = []
            paths.append(row)
            for i in range(m):
                if obstacleGrid[j][i]:
                    row.append(0)
                elif i == 0 and j == 0:
                    row.append(1)
                elif i == 0:
                    row.append(1 if paths[j - 1][i] else 0)
                elif j == 0:
                    row.append(1 if paths[j][i - 1] else 0)
                else:
                    v = paths[j - 1][i] + paths[j][i - 1]
                    row.append(v)
        return paths[n - 1][m - 1]


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    r = s.uniquePathsWithObstacles(obstacleGrid)
    print(r)
    obstacleGrid = [
        [1, 0]
    ]
    r = s.uniquePathsWithObstacles(obstacleGrid)
    print(r)
    obstacleGrid = [
        [1],
        [0]
    ]
    r = s.uniquePathsWithObstacles(obstacleGrid)
    print(r)
