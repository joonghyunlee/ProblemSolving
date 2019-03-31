class Stack:
    def __init__(self):
        self.array = []
        self.mins = []
        self.length = 0

    def push(self, elem):
        if self.length == 0 or self.mins[self.length - 1] > elem:
            self.mins.append(elem)
        else:
            self.mins.append(self.mins[self.length - 1])
        self.array.append(elem)
        self.length += 1

    def pop(self):
        if self.length <= 0:
            raise Exception('Stack is empty')
        self.length -= 1
        self.mins.pop()
        return self.array.pop()

    def min(self):
        return self.mins[self.length - 1]


if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push(1)
    s.push(3)
    print s.min()
    s.push(-1)
    print s.min()
    s.pop()
    print s.min()