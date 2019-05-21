# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, nums):
        nodes = [cls(n) if n else None
                 for n in nums]
        for i, n in enumerate(nodes):
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nodes):
                nodes[i].left = nodes[li]
            if ri < len(nodes):
                nodes[i].right = nodes[ri]
        return nodes[0]


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.prev = []
        self.curr = self.leftmost(root)

    def leftmost(self, node):
        while node and node.left:
            self.prev.append(node)
            node = node.left
        return node

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        resp = self.curr.val
        if self.curr.right:
            self.curr = self.leftmost(self.curr.right)
            return resp
        else:
            if self.prev:
                self.curr = self.prev.pop()
            else:
                self.curr = None
            return resp

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.curr:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == '__main__':
    nums = [7, 3, 15, None, None, 9, 20]
    root = TreeNode.from_list(nums)
    print(root)
    print(root.left)
    print(root.right)
    it = BSTIterator(root)
    # print(it.next())
    # print(it.next())
    while it.hasNext():
        print(it.next())
