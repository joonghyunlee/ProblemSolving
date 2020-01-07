def solution(s):
    n = len(s)
    if n < 1:
        return 0

    answer = 1
    for i in range(n):
        # Case 1
        l = min(i, n - 1 - i)
        c1 = 0
        for j in range(l):
            if s[i - 1 - j] != s[i + 1 + j]:
                break
            c1 += 1

        # Case 2
        l = min(i + 1, n - 1 - i)
        c2 = 0
        for j in range(l):
            if s[i - j] != s[i + 1 + j]:
                break
            c2 += 1

        answer = max(answer, c1 * 2 + 1, c2 * 2)

    return answer


if __name__ == '__main__':
    s = "abcdcba"
    r = solution(s)
    print r
    s = "abacde"
    r = solution(s)
    print r
    s = ""
    r = solution(s)
    print r
    s = "abba"
    r = solution(s)
    print r