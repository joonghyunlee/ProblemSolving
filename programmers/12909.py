def solution(s):
    cnt = 0
    for c in s:
        if c == ')':
            cnt -= 1
        elif c == '(':
            cnt += 1
            
        if cnt < 0:
            return False

        print cnt

    return True if cnt == 0 else False


if __name__ == '__main__':
    r = solution('(())()')
    print r