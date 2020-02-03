def solution(n):
    if n < 0:
        return 0
    pprev, prev = 0, 1
    for _ in range(n):
        pprev, prev = prev, pprev + prev
    return prev % 1234567
    
    
if __name__ == '__main__':
    print(solution(4))
    print(solution(3))