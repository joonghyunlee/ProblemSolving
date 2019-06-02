class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def to_str(self):
        vals = []
        queue = [self]
        while queue:
            node = queue.pop()
            if node is None:
                vals.append(' ')
            else:
                vals.append(str(node.val))
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return ''.join(vals)

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, nums):
        nodes = []
        for n in nums:
            if n is not None:
                nodes.append(cls(n))
            else:
                nodes.append(None)

        for i, node in enumerate(nodes):
            li = 2 * i + 1
            ri = 2 * i + 2
            if node:
                if li < len(nodes):
                    node.left = nodes[li]
                if ri < len(nodes):
                    node.right = nodes[ri]

        return nodes[0]


def checkSubTree(T1, T2):
    S1 = T1.to_str()
    S2 = T2.to_str()

    if S2 in S1:
        return True
    return False


if __name__ == '__main__':
    T1 = TreeNode.from_list([1, 2, 3, 4])
    T2 = TreeNode.from_list([3, 4])
    r = checkSubTree(T1, T2)
    print r
