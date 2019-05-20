class Stack(object):
    def __init__(self):
        self.s = []
        self.temp = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def peek(self):
        if self.s:
            return self.s[-1]
        return None

    def isEmpty(self):
        return True if not self.s else False

    def sort(self):
        while self.s:
            pivot = self.s.pop()
            c = 0
            while self.temp:
                if self.temp[-1] < pivot:
                    break
                self.s.append(self.temp.pop())
                c += 0
            self.temp.append(pivot)
            for _ in range(c):
                self.temp.append(self.s.pop())

        while self.temp:
            self.s.append(self.temp.pop())


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(4)
    s.push(2)
    s.sort()
    while not s.isEmpty():
        print s.pop()
