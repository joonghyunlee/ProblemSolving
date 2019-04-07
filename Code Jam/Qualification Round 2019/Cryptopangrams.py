def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def decrypt(n, l, text):
    cs = [None for _ in range(l + 1)]
    for i in range(l-1):
        if text[i] != text[i + 1]:
            cs[i + 1] = gcd(text[i], text[i + 1])
            cs[i] = text[i] // cs[i + 1]
            break

    for j in range(i - 1, -1, -1):
        cs[j] = text[j] // cs[j + 1]
    for j in range(i + 1, l):
        cs[j + 1] = text[j] // cs[j]

    primes = sorted(set(cs))
    message = []
    for i in range(l + 1):
        c = chr(primes.index(cs[i]) + ord('A'))
        message.append(c)
    return ''.join(message)


if __name__ == '__main__':
    T = int(raw_input())
    Ns, Ls, texts = [], [], []
    for i in range(T):
        N, L = raw_input().split()
        Ns.append(int(N)), Ls.append(int(L))
        text = raw_input().split()
        texts.append([int(text[x]) for x in range(int(L))])

    for i in range(T):
        print "Case #{}: {}".format(i+1, decrypt(Ns[i], Ls[i], texts[i]))
