def solution(distance, rocks, n):
    rocks.sort()
    l, r = 1, distance
    while l + 1 < r:
        m = (l + r) // 2
        prev = 0
        count = 0
        for curr in rocks:
            if curr - prev < m:
                count += 1
            else:
                prev = curr
        
        if distance - prev < m:
            count += 1

        if count <= n:
            l = m
        else:
            r = m

    return l


if __name__ == '__main__':
    rocks = [2, 14, 11, 21, 17]
    r = solution(25, rocks, 2)
    print(r)