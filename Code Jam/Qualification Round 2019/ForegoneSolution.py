# t = int(raw_input()) # read a line with a single integer
# for i in xrange(1, t + 1):
#    n, m = [int(s) for s in raw_input().split(" ")]
# read a list of integers, 2 in this case
#    print "Case #{}: {} {}".format(i, n + m, n * m)
#    # check out .format's specification for more formatting options


def divide_two(num):
    a, b = [], []
    for c in num:
        if c == '4':
            a.append('3')
            b.append('1')
        else:
            a.append(c)
            if b:
                b.append('0')

    return list(a), list(b)


if __name__ == '__main__':
    T = int(raw_input())
    Ns = []
    for i in range(1, T + 1):
        Ns.append(raw_input())

    for i, N in enumerate(Ns):
        a, b = divide_two(N)
        print "Case #{}: {} {}".format(i+1, ''.join(a), ''.join(b))
