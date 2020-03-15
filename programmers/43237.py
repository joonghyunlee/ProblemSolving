def solution(budgets, M):
    over = sum(budgets) - M
    if over <= 0:
        return max(budgets)
    budgets.sort(reverse=True)
    n = len(budgets)
    x = budgets[0]
    step = 1
    for i in range(n):
        if i == n - 1:
            return M // n
        if over <= step  * (budgets[i] - budgets[i + 1]):
            x -= (over // step) + 1
            break
        else:
            over -= step * (budgets[i] - budgets[i + 1])
            step += 1
            x -= (budgets[i] - budgets[i + 1])
    return x


if __name__ == '__main__':
    budgets = [120, 110, 140, 150]
    r = solution(budgets, 485)
    print r
