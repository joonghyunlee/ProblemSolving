class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.insert(0, x)
        for i in range(self.len):
            self.queue.insert(0, self.queue.pop())
        self.len += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x = self.queue.pop()
        if x: self.len -= 1
        return x

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[-1] if self.len else None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    print s.top()
    print s.pop()
    print s.empty()
