def solution(N):
    lengths = [1, 1]
    w, h = 1, 1

    for i in range(2, N):
        lengths.append(lengths[i - 1] + lengths[i - 2])

    for i in range(N - 1):
        if i % 2:
            w += lengths[i + 1]
        else:
            h += lengths[i + 1]
        
    return 2 * h + 2 * w


if __name__ == '__main__':
    r = solution(1)
    print r
    r = solution(2)
    print r
    r = solution(3)
    print r
    r = solution(4)
    print r