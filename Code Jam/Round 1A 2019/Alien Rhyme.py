class Node:
    def __init__(self, c):
        self.val = c
        self.end = False
        self.next = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = Node(None)

    def add(self, s):
        p = self.root
        for c in s:
            i = ord(c) - ord('A')
            if p.next[i] is None:
                p.next[i] = Node(c)
            p = p.next[i]
        p.end = True

    def calculate(self):
        def helper(node):
            c = 0
            for n in node.next:
                if n:
                    c += helper(n)
            if node.end:
                c += 1
            if node != self.root and c >= 2:
                c -= 2
            return c
        return helper(self.root)


if __name__ == '__main__':
    T = int(raw_input())
    tests = []
    for i in range(T):
        N = int(raw_input())
        words = [raw_input() for _ in range(N)]
        tests.append((N, words))

    for i in range(T):
        N, words = tests[i]
        trie = Trie()
        for w in words:
            trie.add(w[::-1])

        print 'Case #{}: {}'.format(i + 1, N - trie.calculate())
