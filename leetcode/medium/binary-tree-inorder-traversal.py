# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inorder(p):
            if not p:
                return
            if not p.left and not p.right:
                res.append(p.val)
                return
            if p.left:
                inorder(p.left)
            res.append(p.val)
            if p.right:
                inorder(p.right)
        inorder(root)
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    r = s.inorderTraversal(root)
    print r
