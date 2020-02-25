class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        memo = [[0] * N for _ in range(N)]
        mines = set((mine[0], mine[1]) for mine in mines)

        # left & right
        for i in range(N):
            count = 0
            for j in range(N):
                count = 0 if (i, j) in mines else count + 1
                memo[i][j] = count
            count = 0
            for j in range(N - 1, -1, -1):
                count = 0 if (i, j) in mines else count + 1
                memo[i][j] = min(memo[i][j], count)

        # up & down
        for j in range(N):
            count = 0
            for i in range(N):
                count = 0 if (i, j) in mines else count + 1
                memo[i][j] = min(memo[i][j], count)
            count = 0
            for i in range(N - 1, -1, -1):
                count = 0 if (i, j) in mines else count + 1
                memo[i][j] = min(memo[i][j], count)

        print memo
        return max(max(row) for row in memo)


if __name__ == '__main__':
    s = Solution()
    r = s.orderOfLargestPlusSign(5, [[4, 2]])
    print r
    r = s.orderOfLargestPlusSign(2, [])
    print r
    r = s.orderOfLargestPlusSign(1, [[0, 0]])
    print r
    r = s.orderOfLargestPlusSign(5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 0],
                                     [1, 1], [1, 2], [1, 3], [1, 4], [2, 0],
                                     [2, 1], [2, 3], [2, 4], [3, 1], [3, 2],
                                     [3, 3], [3, 4], [4, 0], [4, 1], [4, 2],
                                     [4, 3], [4, 4]])
    print r
    r = s.orderOfLargestPlusSign(
        5, [[1, 0], [1, 4], [2, 4], [3, 2], [4, 0], [4, 3]])
    print r
    r = s.orderOfLargestPlusSign(2, [[0, 0], [0, 1], [1, 0]])
    print r
    r = s.orderOfLargestPlusSign(2, [[0, 1], [1, 0], [1, 1]])
    print r
    r = s.orderOfLargestPlusSign(3, [[0, 1]])
    print r