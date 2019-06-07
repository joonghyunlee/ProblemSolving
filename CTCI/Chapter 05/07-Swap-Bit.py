# n
# 0 -> 1, 1 <- 0
# odd_mask = 0101010101
# even_mask = 1010101010
# n & odd_mask
# n & even_mask
# ((n & odd_mask) << 1) | ((n & even_mask) >> 1)


def swap_bit(n):
    odd_mask = 0x55555555
    even_mask = 0xAAAAAAAA

    return ((n & odd_mask) << 1) | ((n & even_mask) >> 1)


if __name__ == '__main__':
    n = 23420786
    print '{0:032b}'.format(n)
    r = swap_bit(n)
    print '{0:032b}'.format(r)
