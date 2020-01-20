def solution(n, s):
    # a + b = s
    # a * b = a * (s - a) = sa - a^2
    # max(sa - a^2) if s - 2a == 0
    if s // n == 0:
        return [-1]

    answer = [s // n] * n
    residue = s % n
    for i in range(residue):
        answer[n - 1 - i] += 1
    
    return answer


if __name__ == '__main__':
    print solution(2, 9)
    print solution(2, 1)
    print solution(2, 8)