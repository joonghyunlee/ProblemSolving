def solution(strs, t):
    n = len(t)
    memo = [float("inf")] * (n + 1)
    memo[0] = 0
    for i in range(n + 1):
        for s in strs:
            l = len(s)
            if i + l < n + 1 and t[i:i + l] == s:
                memo[i + l] = min(memo[i + l], memo[i] + 1)
    return memo[n] if memo[n] < float("inf") else -1


def solution2(strs, t):
    n = len(t)
    memo = [float("inf")] * (n + 1)
    memo[0] = 0
    sizes = set(len(s) for s in strs)
    strs = set(strs)
    for i in range(n + 1):
        for size in sizes:
            if i + size < n + 1 and t[i:i + size] in strs:
                memo[i + size] = min(memo[i + size], memo[i] + 1)
    return memo[n] if memo[n] < float("inf") else -1


if __name__ == '__main__':
    strs = ["ba", "na", "n", "a"]
    r = solution(strs, "banana")
    print r
    r = solution2(strs, "banana")
    print r
    strs = ["app", "ap", "p", "l", "e", "ple", "pp"]
    r = solution(strs, "apple")
    print r
    r = solution2(strs, "apple")
    print r
    strs = ["ba", "an", "nan", "ban", "n"]
    r = solution(strs, "banana")
    print r
    r = solution2(strs, "banana")
    print r