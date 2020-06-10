class Solution:
    def findCircleNum(self, M: 'List[List[int]]') -> int:
        def helper(start):
            queue = [start]
            cnt = 0
            while queue:
                row = queue.pop()
                for col, val in enumerate(M[row]):
                    if val == 0:
                        continue
                    cnt += 1
                    M[row][col] = 0
                    if row != col and col not in visited:
                        visited.add(col)
                        queue.insert(0, col)
            return cnt > 0

        n = len(M)
        cnt = 0
        visited = set()
        for i in range(n):
            if helper(i):
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    r = s.findCircleNum(M)
    print(r)
    M = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    r = s.findCircleNum(M)
    print(r)
