import sys


def rl():
    return sys.stdin.readline()


def match(n, russians, koreans):
    russians.sort()
    koreans.sort()

    s = 0
    while koreans:
        k = koreans.pop()
        while russians:
            r = russians.pop()
            if k >= r:
                s += 1
                break

    return s

if __name__ == '__main__':
    cases = int(rl())

    result = []
    for case in range(cases):
        n = int(rl())
        russians = map(int, rl().split())
        koreans = map(int, rl().split())
        r = match(n, russians, koreans)
        result.append(r)

    print '\n'.join(map(str, result))
    