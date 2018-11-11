# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traversal(r, depth):
            if not r:
                return depth
            return max(traversal(r.left, depth + 1),
                       traversal(r.right, depth + 1))

        return traversal(root, 0)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.maxDepth(root)
    print r
    root = TreeNode(3)
    r = s.maxDepth(root)
    print r
    root = None
    r = s.maxDepth(root)
    print r
