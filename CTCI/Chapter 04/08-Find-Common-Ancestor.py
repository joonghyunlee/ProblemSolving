class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(self, nums):
        nodes = []
        for n in nums:
            if n is not None:
                nodes.append(TreeNode(n))
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


def commonAncestor(root, nodeA, nodeB):
    def helper(node, A):
        if node is None:
            return False
        if node == A:
            return True
        return helper(node.left, A) or helper(node.right, A)

    if root is None or root == nodeA or root == nodeB:
        return root

    inA = helper(root.left, nodeA)
    inB = helper(root.left, nodeB)
    if (inA and not inB) or (not inA and inB):
        return root

    if inA and inB:
        return commonAncestor(root.left, nodeA, nodeB)

    return commonAncestor(root.right, nodeA, nodeB)


def commonAncestor2(root, nodeA, nodeB):
    def helper(root, nodeA, nodeB):
        if root is None:
            return None, False
        if root == nodeA and root == nodeB:
            return root, True

        nl, isAncestor = helper(root.left, nodeA, nodeB)
        if isAncestor:
            return nl, isAncestor

        nr, isAncestor = helper(root.right, nodeA, nodeB)
        if isAncestor:
            return nr, isAncestor

        if nl is not None and nr is not None:
            return root, True
        elif root == nodeA or root == nodeB:
            return root, (nl is not None or nr is not None)

        if nl is not None:
            return nl, False
        return nr, False
    ancestor, isAncestor = helper(root, nodeA, nodeB)
    if isAncestor:
        return ancestor
    return None


if __name__ == '__main__':
    nums = [20, 10, 30, 5, 15, None, None, 3, 7, None, 17]
    root = TreeNode.from_list(nums)
    p = root.left.right.right
    q = root.left.left.right
    r = commonAncestor(root, p, q)
    print r
    r = commonAncestor2(root, p, q)
    print r
