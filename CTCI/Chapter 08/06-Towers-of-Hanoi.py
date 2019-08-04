# 1: [1] [] [] -> [] [] [1]
# 2: [2, 1] [] [] -> [2] [1] [] -> [] [1] [2] -> [] [] [2, 1]
# 3: [3, 2, 1] [] [] -> [3, 2] [1] [] -> [3] [1] [2] -> [3, 1] [] [] -> [] []


class Solver(object):
    def __init__(self, n):
        self.disks = n
        self.stacks = [[i for i in range(n, 0, -1)], [], []]

    def solve(self):
        def helper(n, source, buffer, destination):
            if n == 0:
                return

            helper(n - 1, source, destination, buffer)
            self.stacks[destination].append(self.stacks[source].pop())
            helper(n - 1, buffer, source, destination)

        helper(self.disks, 0, 1, 2)

    def show(self):
        print self.stacks


if __name__ == '__main__':
    s = Solver(10)
    s.solve()
    s.show()
