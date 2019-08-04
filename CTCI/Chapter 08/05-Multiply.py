# a, b
# sum = a + a + .. + a


def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result


# a, b
# i th of b is 1: a << i
# for all bits of b
# sum
def multiply2(a, b):
    result = 0
    mask = 0b1
    i = 0
    while mask <= b:
        if mask & b:
            result += (a << i)
        mask <<= 1
        i += 1
    return result
