class Solution:
    def countServers(self, grid: 'List[List[int]]') -> int:
        visited = set()

        def helper(n: int, m: int, r: int, c: int):
            if (r, c) in visited:
                return
            nexts = set()
            for i in range(n):
                if i != r and grid[i][c] == 1:
                    nexts.add((i, c))
            for i in range(m):
                if i != c and grid[r][i] == 1:
                    nexts.add((r, i))
            if nexts:
                visited.add((r, c))
                visited.union(nexts)

        n, m = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            for c, computer in enumerate(row):
                if computer == 1:
                    helper(n, m, r, c)

        return len(visited)

    def countServers2(self, grid: 'List[List[int]]') -> int:
        x, y = tuple(map(sum, grid)), tuple(map(sum, zip(*grid)))
        connected = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and x[r] + y[c] > 2:
                    connected += 1
        return connected


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 0], [0, 1]]
    r = s.countServers(grid)
    print(r)
    r = s.countServers2(grid)
    print(r)
    grid = [[1, 0], [1, 1]]
    r = s.countServers(grid)
    print(r)
    r = s.countServers2(grid)
    print(r)
    grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    r = s.countServers(grid)
    print(r)
    r = s.countServers2(grid)
    print(r)
