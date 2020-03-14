def solution(triangle):
    memo = [triangle[0][0]]
    for row in triangle[1:]:
        newMemo = []
        for j, col in enumerate(row):
            value = 0
            if j - 1 >= 0:
                value = max(value, col + memo[j - 1])
            if j < len(memo):
                value = max(value, col + memo[j])
            newMemo.append(value)
        memo = newMemo
    return max(memo)


if __name__ == '__main__':
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    r = solution(triangle)
    print r
