def find1(msg):
    cmap = [False for _ in range(128)]
    for c in msg:
        key = ord(c)
        if cmap[key]:
            return True
        else:
            cmap[key] = True

    return False

def find2(msg):
    p = None
    for c in sorted(msg):
        if p == c:
            return True
        else:
            p = c
    return False


if __name__ == '__main__':
    MAX_SIZE = 10
    import random, string
    msg = ''.join([random.choice(string.ascii_letters + string.digits)
                   for _ in range(MAX_SIZE)])
    print msg
    r = find1(msg)
    print r
    r = find2(msg)
    print r
