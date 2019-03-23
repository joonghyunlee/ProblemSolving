def convert(url, length):
    ni = len(url)
    for i in reversed(range(length)):
        if url[i] != ' ':
            url[ni - 1] = url[i]
            ni -= 1
        else:
            url[ni - 3:ni] = '%20'
            ni -= 3
    return url


if __name__ == '__main__':
    url = '/abc/system name/disk name/partition name      '
    r = convert(list(url), 41)
    print ''.join(r)
