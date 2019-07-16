# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ts = 0
        stack = []
        v, n = 0, root
        while True:
            if n:
                v = v * 10 + n.val
                stack.append((v, n))
                n = n.left
            elif stack:
                v, n = stack.pop()
                if not n.left and not n.right:
                    ts += v

                n = n.right
            else:
                break
        return ts


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    r = s.sumNumbers(root)
    print r
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    r = s.sumNumbers(root)
    print r
