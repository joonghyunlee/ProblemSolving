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
        nodes = [cls(n) if n else None for n in nums]
        for i, n in enumerate(nodes):
            if n is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            n.left = nodes[li] if li < len(nodes) else None
            n.right = nodes[ri] if ri < len(nodes) else None
        return nodes[0]


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        p = root
        while p:
            if p.val == val:
                return p
            elif p.val > val:
                p = p.left
            else:
                p = p.right
        return None


if __name__ == '__main__':
    s = Solution()
    root = TreeNode.from_list([4, 2, 7, 1, 3])
    r = s.searchBST(root, 2)
    print r
