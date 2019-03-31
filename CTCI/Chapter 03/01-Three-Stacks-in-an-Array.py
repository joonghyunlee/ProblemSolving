NUMS_STACK = 3
STACK_SIZE = 10


class MultiStack:
    def __init__(self):
        self.array = [None] * (STACK_SIZE * NUMS_STACK)
        self.sizes = [0] * NUMS_STACK

    def is_empty(self, stack_num):
        if self.sizes[stack_num] > 0:
            return False
        return True

    def push(self, stack_num, elem):
        if self.sizes[stack_num] == STACK_SIZE:
            raise Exception('Stack is full')
        self.array[stack_num * STACK_SIZE + self.sizes[stack_num]] = elem
        self.sizes[stack_num] += 1
        print self.array

    def pop(self, stack_num):
        if self.sizes[stack_num] == 0:
            raise Exception('Stack is empty')
        elem = self.array[stack_num * STACK_SIZE + self.sizes[stack_num] - 1]
        self.sizes[stack_num] -= 1
        return elem


if __name__ == '__main__':
    ms = MultiStack()
    print ms.is_empty(0)
    print ms.is_empty(1)
    print ms.is_empty(2)
    ms.push(2, 1)
    print ms.is_empty(2)
    ms.push(1, 1)
    print ms.pop(2)
    ms.push(0, 2)
    print ms.pop(1)
    print ms.pop(0)