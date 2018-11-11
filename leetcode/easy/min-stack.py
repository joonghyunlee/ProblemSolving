class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        pos = 0
        for i in range(len(self.list)):
            if x > self.list[i]:
                pos = i
                break
        print "push - pos: ", pos
        print "push - self.list: ", self.list
        self.list.insert(pos, x)
        print "push - self.list: ", self.list

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        self.list.remove(x)
        print "pop - self.list: ", self.list

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        print "getMin - self.list: ", self.list
        return self.list[-1]


if __name__ == '__main__':
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print ms.getMin()
    #ms.pop()
    #print ms.top()
    #print ms.getMin()
