def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    for move in moves:
        find = False
        for i in range(n):
            if board[i][move - 1] != 0:
                find = True
                break
        if not find:
            continue
        if stack and stack[-1] == board[i][move - 1]:
            stack.pop()
            answer += 2
        else:
            stack.append(board[i][move - 1])
        board[i][move - 1] = 0
    return answer


if __name__ == '__main__':
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1]
    ]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    r = solution(board, moves)
    print r
