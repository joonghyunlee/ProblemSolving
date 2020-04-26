class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0]) if r > 0 else 0
        if r <= 2 or c <= 2:
            return

        unflipped = set()
        for row in [0, r - 1]:
            for col in range(c):
                if board[row][col] == 'O':
                    unflipped.add((row, col))
        for col in [0, c - 1]:
            for row in range(r):
                if board[row][col] == 'O':
                    unflipped.add((row, col))

        for row, col in list(unflipped):
            queue = [(row, col)]
            while queue:
                tr, tc = queue.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if not (0 <= tr + dr < r and 0 <= tc + dc < c):
                        continue
                    elif board[tr + dr][tc + dc] == 'O' \
                        and (tr + dr, tc + dc) not in unflipped:
                        unflipped.add((tr + dr, tc + dc))
                        queue.insert(0, (tr + dr, tc + dc))

        for row in range(r):
            for col in range(c):
                if board[row][col] == 'O' and (row, col) not in unflipped:
                    board[row][col] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    s.solve(board)
    print board
    board = [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O']
    ]
    s.solve(board)
    print board
    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"]
    ]
    s.solve(board)
    print board
