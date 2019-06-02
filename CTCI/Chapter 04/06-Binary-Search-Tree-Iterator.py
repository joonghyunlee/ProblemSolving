# node.right -> leftmost(node.right)
# node.right is None
# -> if left chid: node.parent
# -> if right child: up until i am left child parent


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, nums):
        nodes = []
        for n in nums:
            if n is not None:
                nodes.append(cls(n))
            else:
                nodes.append(n)

        for i, n in enumerate(nodes):
            li = i * 2 + 1
            ri = i * 2 + 2
            if li < len(nodes):
                n.left = nodes[li]
            if ri < len(nodes):
                n.right = nodes[ri]
        return nodes[0]


def nextNode(node):
    def leftmost(node):
        lchild = node
        while lchild.left:
            lchild = lchild.left
        return lchild

    if node.right:
        return leftmost(node.right)

    np = node.parent
    while np:
        if np.left == node:
            return np
        np = np.parent

    return np


if __name__ == '__main__':
    root = TreeNode.from_list([5, 3, 7, 1, 4, 6, 8])
    n = nextNode(root)
    print n
    n = nextNode(root.right)
    print n
