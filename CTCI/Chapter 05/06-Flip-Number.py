def flipNumber(a, b):
    r = a ^ b
    mask = 0b1
    count = 0
    while mask < r:
        if mask & r:
            count += 1
        mask <<= 1
    return count


if __name__ == '__main__':
    r = flipNumber(15, 29)
    print r
