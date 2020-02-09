def changeCoin(coins, n):
    def helper(n, coins):
        if len(coins) == 1:
            return 1
        total = 0
        coin = coins.pop()
        for i in range(0, n, coin):
            total += helper(n - i, coins[:])
        return total

    coins.sort()
    return helper(n, coins)


def changeCoin3(coins, n):
    def helper(n, i):
        if i >= len(coins) - 1:
            return 1
        total = 0
        for j in range(0, n, coins[i]):
            total += helper(n - j, i + 1)
        return total

    return helper(n, 0)


def changeCoin2(coins, n):
    memo = [[0] * len(coins) for _ in range(n + 1)]

    def helper(n, i):
        if memo[n][i]:
            return memo[n][i]
        if i >= len(coins) - 1:
            return 1
        total = 0
        for j in range(0, n, coins[i]):
            total += helper(n - j, i + 1)
        memo[n][i] = total
        return total

    return helper(n, 0)


if __name__ == '__main__':
    print changeCoin([25, 10, 5, 1], 124)
    print changeCoin2([25, 10, 5, 1], 124)
    print changeCoin3([25, 10, 5, 1], 124)