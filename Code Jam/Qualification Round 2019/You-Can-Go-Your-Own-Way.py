def my_way(n, path):
    steps = []
    for i in range(2 * n - 2):
        steps.append('E' if path[i] == 'S' else 'S')
    return steps

if __name__ == '__main__':
    T = int(raw_input())
    Ps, Paths = [], []
    for i in range(1, T + 1):
        Ps.append(int(raw_input()))
        Paths.append(raw_input())

    for i in range(T):
        steps = my_way(Ps[i], Paths[i])
        print "Case #{}: {}".format(i+1, ''.join(steps))
