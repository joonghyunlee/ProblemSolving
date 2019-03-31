class QueueViaStacks:
    def __init__(self):
        self.active = []
        self.inactive = []

    def push(self, x):
        while self.inactive:
            self.active.append(self.inactive.pop())
        self.active.append(x)

    def pop(self):
        while self.active:
            self.inactive.append(self.active.pop())
        return self.inactive.pop()


if __name__ == '__main__':
    q = QueueByStacks()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.pop()
    q.push(4)
    q.push(5)
    print q.pop()
    print q.pop()
    print q.pop()