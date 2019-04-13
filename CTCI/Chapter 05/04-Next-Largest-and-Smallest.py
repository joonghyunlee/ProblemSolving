# 11011001111100
# 11011010001111


def next_largest(n):
    c1, c0 = 0, 0
    mask = 0b1
    while n >= mask and n & mask == 0:
        c0 += 1
        mask <<= 1
    while n >= mask and n & mask:
        c1 += 1
        mask <<= 1
    return n + ((1 << c0) - 1) + 1 + ((1 << (c1 - 1)) - 1)

# A = 11011000000111
# B = 11010000001111


def next_smallest(n):
    c1, c0 = 0, 0
    mask = 0b1
    while n >= mask and n & mask:
        c1 += 1
        mask <<= 1
    while n >= mask and n & mask == 0:
        c0 += 1
        mask <<= 1
    return n - (1 << c1) - (1 << (c0 - 1)) + 1


if __name__ == '__main__':
    r = next_largest(0b10011101110000)
    print '{0:b}'.format(r)
    r = next_smallest(0b10011110001111)
    print '{0:b}'.format(r)
