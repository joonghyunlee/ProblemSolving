class Solution:
    def closedIsland(self, grid: 'List[List[int]]') -> int:
        def helper(r, c):
            if grid[r][c] != 0:
                return False
            grid[r][c] = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    helper(r + dr, c + dc)
            return True

        m = len(grid)
        n = len(grid[0]) if grid else 0
        # border
        for r in range(m):
            helper(r, 0)
            helper(r, n - 1)
        for c in range(n):
            helper(0, c)
            helper(m - 1, c)

        island = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if helper(r, c):
                    island += 1
        return island


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
    ]
    r = s.closedIsland(grid)
    print(r)