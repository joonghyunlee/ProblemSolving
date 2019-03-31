class SetOfStacks:
    def __init__(self, capacity=10):
        self.stacks = [[]]
        self.sizes = [0]
        self.limit = capacity
        self.cur_stack_num = 0

    def push(self, elem):
        if self.sizes[self.cur_stack_num] == self.limit:
            self.stacks.append([])
            self.sizes.append(0)
            self.cur_stack_num += 1
        self.stacks[self.cur_stack_num].append(elem)
        self.sizes[self.cur_stack_num] += 1

    def pop(self):
        if self.sizes[self.cur_stack_num] == 0:
            if self.cur_stack_num == 0:
                raise Exception('Stack is empty')
            self.stacks.pop()
            self.sizes.pop()
            self.cur_stack_num -= 1
        elem = self.stacks[self.cur_stack_num].pop()
        self.sizes[self.cur_stack_num] -= 1
        return elem


if __name__ == '__main__':
    s = SetOfStacks(3)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print s.pop()
    print s.pop()

    for i in range(20):
        s.push(i)

    for _ in range(10):
        print s.pop()