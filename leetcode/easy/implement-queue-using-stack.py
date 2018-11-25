class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        ts = []
        for i in range(self.len):
            ts.append(self.stack.pop())
        self.stack.append(x)
        for i in range(self.len):
            self.stack.append(ts.pop())
        self.len += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        x = self.stack.pop()
        self.len -= 1
        return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.len == 0


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print q.peek()
    print q.pop()
    print q.empty()
