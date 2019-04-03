def insertNumber(n, m, i, j):
    mask = ~(((1 << (j+1)) - 1) ^ ((1 << i) - 1))
    return (n & mask) | (m << i)


if __name__ == '__main__':
    r = insertNumber(0b10000000000, 0b10011, 2, 6)
    print '{0:b}'.format(r)
