def getMaximumLength(x):
    c, m, p = 0, 0, 0
    mask = 0b1
    while x >= mask:
        if x & mask > 0:
            c += 1
        else:
            m = max(m, p + c + 1)
            p = c
            c = 0
        mask <<= 1
    return max(m, p + c + 1)


if __name__ == '__main__':
    r = getMaximumLength(0b11011001110)
    print r
