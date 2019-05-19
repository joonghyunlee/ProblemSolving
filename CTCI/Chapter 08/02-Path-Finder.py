class PathFinder:
    def __init__(self, m):
        self.map = m
        self.r = len(m)
        self.c = len(m[0] if m else 0)

    def find(self):
        def helper(x, y):
            if x + 1 > self.r or y + 1 > self.c or self.map[x][y] > 0:
                return False

            if (x, y) in visited:
                return False

            if x == self.r - 1 and y == self.c - 1:
                paths.append((x, y))
                return True
            elif helper(x + 1, y) or helper(x, y + 1):
                paths.append((x, y))
                return True

            visited.append((x, y))
            return False

        if not m:
            return None

        paths = []
        visited = []
        helper(0, 0)
        print paths


if __name__ == '__main__':
    m = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    p = PathFinder(m)
    p.find()
