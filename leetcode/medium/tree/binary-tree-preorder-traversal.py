# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        s, r = [root], []
        while s:
            p = s.pop()
            r.append(p.val)

            if p.right:
                s.append(p.right)
            if p.left:
                s.append(p.left)

        return r


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    r = s.preorderTraversal(root)
    print r
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    r = s.preorderTraversal(root)
    print r
