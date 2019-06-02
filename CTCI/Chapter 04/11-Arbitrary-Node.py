import random


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 1

    def __repr__(self):
        return str('{}'.format(self.val))


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = TreeNode(x)
            return

        p = self.root
        while p:
            p.size += 1
            if p.val > x:
                if p.left is None:
                    p.left = TreeNode(x)
                    return
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = TreeNode(x)
                    return
                else:
                    p = p.right

    def find(self, x):
        p = self.root
        while p:
            if p.val == x:
                return p
            elif p.val > x:
                p = p.left
            else:
                p = p.right
        return None

    def get(self, i):
        p = self.root
        while p:
            ls = p.left.size if p.left else 0
            if i < ls:
                p = p.left
            elif i == ls:
                return p
            else:
                i -= (ls + 1)
                p = p.right
        return None

    def pick(self):
        p = self.root
        i = random.randrange(0, p.size)
        return self.get(i)

    def show(self):
        def helper(node):
            if node is None:
                return

            helper(node.left)
            print node,
            helper(node.right)
        helper(self.root)
        print


if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(20)
    bt.insert(10)
    bt.insert(30)
    bt.insert(5)
    bt.insert(7)
    bt.insert(3)
    bt.insert(15)
    bt.insert(17)
    bt.insert(35)
    bt.show()
    print bt.find(35)
    print bt.find(34)
    print bt.get(0)
    print bt.get(1)
    print bt.pick()
    print bt.pick()
