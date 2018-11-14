class MinStack(object):

    class StackNode(object):
        def __init__(self, x, m, n=None):
            self.val = x
            self.min = m if m < x else x
            self.next = n

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.head:
            p = self.StackNode(x, self.head.min, self.head)
            self.head = p
        else:
            self.head = self.StackNode(x, x)

    def pop(self):
        """
        :rtype: void
        """
        if self.head:
            self.head = self.head.next

    def top(self):
        """
        :rtype: int
        """
        return self.head.val if self.head else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.head.min if self.head else None

    def printStack(self):
        p = self.head
        print "Stack: ",
        while p:
            print p.val,
            p = p.next
        print


if __name__ == '__main__':
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-1)
    ms.printStack()
    print ms.getMin()
    print ms.top()
    ms.pop()
    print ms.getMin()
