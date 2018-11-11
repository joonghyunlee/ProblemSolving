class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare1(lnode, rnode):
            if not lnode and not rnode:
                return True
            elif ((not lnode and rnode) or
                    (lnode and not rnode)):
                return False

            if lnode.val != rnode.val:
                return False

            return (compare1(lnode.left, rnode.right) and
                    compare1(lnode.right, rnode.left))

        if not root:
            return True

        lp = root.left
        rp = root.right

        return compare1(lp, rp)


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    r = s.isSymmetric(root)
    print r
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    r = s.isSymmetric(root)
    print r
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(2)
    r = s.isSymmetric(root)
    print r
    root = TreeNode(1)
    root.left = TreeNode(2)
    r = s.isSymmetric(root)
    print r
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    r = s.isSymmetric(root)
    print r
