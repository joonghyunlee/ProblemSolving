class Permutation:
    def __init__(self, word):
        self.length = len(word)
        self.cmap = dict()
        for c in word:
            v = self.cmap.get(c, None)
            if v is None:
                self.cmap[c] = 1
            else:
                self.cmap[c] = v + 1
        self.perms = []

    def get(self):
        def helper(prefix, length):
            if length == 0:
                self.perms.append(prefix)
                return
            for c, v in self.cmap.items():
                if v > 0:
                    self.cmap[c] = v - 1
                    helper(prefix + c, length - 1)
                    self.cmap[c] = v
        helper('', self.length)

        print self.perms


if __name__ == '__main__':
    s = Permutation('python')
    s.get()
