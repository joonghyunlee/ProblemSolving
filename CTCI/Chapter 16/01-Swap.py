def swap(a, b):
    a, b = (a ^ b) ^ a, (a ^ b) ^ b
    return a, b


if __name__ == '__main__':
    print swap(3, 5)
