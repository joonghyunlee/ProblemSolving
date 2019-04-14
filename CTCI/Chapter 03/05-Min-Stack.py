class MinStack:
    def __init__(self):
        self.stack = []
        self.backup = []

    def push(self, elem):
        while self.stack:
            if self.peek() > elem:
                break
            self.backup.append(self.stack.pop())
        self.stack.append(elem)
        while self.backup:
            self.stack.append(self.backup.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return not self.stack


if __name__ == '__main__':
    ms = MinStack()
    ms.push(1)
    ms.push(2)
    ms.push(3)
    ms.push(4)
    print ms.peek()
    print ms.pop()
    print ms.pop()
