class Set:
    def printSubSet(self, s):
        n = len(s)
        for i in range(2 ** n):
            sub = []
            mask = 0b1
            for j, e in enumerate(s):
                if (mask << j) & i:
                    sub.append(e)
            print sub


if __name__ == '__main__':
    s = Set()
    s.printSubSet((1, 2, 3, 4, 5, 6))
