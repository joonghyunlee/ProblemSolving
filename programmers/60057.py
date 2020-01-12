def solution(s):
    n = len(s)
    min_len = n
    for size in range(1, n // 2 + 1):
        nl = 0
        pattern = s[:size]
        freq = 1
        for i in range(size, n, size):
            if pattern == s[i:i + size]:
                freq += 1
            else:
                nl += len(str(freq)) + size if freq > 1 else size
                pattern = s[i:i + size]
                freq = 1

        nl += len(pattern) + len(str(freq)) if freq > 1 else len(pattern)

        min_len = min(min_len, nl)

    return min_len


if __name__ == '__main__':
    r = solution('aabbaccc')
    print r
    r = solution('ababcdcdababcdcd')
    print r
    r = solution('abcabcdede')
    print r
    r = solution('abcabcabcabcdededededede')
    print r
    r = solution('xababcdcdababcdcd')
    print r
    r = solution(''.join(['a' for _ in range(100)]))
    print r
    r = solution('aaaaaaaaaa')
    print r
    r = solution('a')
    print r
