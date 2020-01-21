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
        nodes = [cls(num) if num is not None else None for num in nums]
        n = len(nodes)
        for i, node in enumerate(nodes):
            if node is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < n:
                node.left = nodes[li]
            if ri < n:
                node.right = nodes[ri]

        return nodes[0] if nodes else None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def recursion(prev, curr):
            prev.left, prev.right = None, curr
            left, right = curr.left, curr.right
            if left and not right:
                node = recursion(curr, left)
            elif not left and right:
                node = recursion(curr, right)
            elif left and right:
                node = recursion(curr, left)
                node = recursion(node, right)
            else:
                node = curr
            return node

        if not root:
            return

        head = TreeNode(None)
        recursion(head, root)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode.from_list([1, 2, 5, 3, 4, None, 6])
    s.flatten(root)
    node = root
    while node:
        print node,
        node = node.right
    print

    root = TreeNode.from_list([1, 2, None, 3, 4, None, None, 5])
    s.flatten(root)
    node = root
    while node:
        print node,
        node = node.right
    print
