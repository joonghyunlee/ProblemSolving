def convertToBinaryRepr(num):
    s, d = ['0.'], 0.5
    while num > 0:
        if len(s) > 30:
            return 'ERROR'
        if num >= d:
            num -= d
            s.append('1')
        else:
            s.append('0')
        d /= 2
        print d
        print s

    return ''.join(s)


if __name__ == '__main__':
    f = 0.75
    r = convertToBinaryRepr(f)
    print r
