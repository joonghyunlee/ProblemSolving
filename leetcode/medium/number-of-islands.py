class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        def helper(row, col):
            if grid[row][col] == '0':
                return
            m, n = len(grid), len(grid[0]) if grid else 0
            q = [(row, col)]
            grid[row][col] = '0'
            while q:
                r, c = q.pop()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= r + dr < m and 0 <= c + dc < n:
                        if grid[r + dr][c + dc] == '1':
                            grid[r + dr][c + dc] = '0'
                            q.insert(0, (r + dr, c + dc))

        m, n = len(grid), len(grid[0]) if grid else 0
        num = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    helper(row, col)
                    num += 1
        return num


if __name__ == '__main__':
    s = Solution()
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    r = s.numIslands(grid)
    print(r)
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    r = s.numIslands(grid)
    print(r)