# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        values = []
        if root:
            stack.append((0, root))

        while len(stack) > 0:
            depth, parent = stack.pop()

            if depth >= len(values):
                values.insert(depth, [])
            values[depth].append(parent.val)

            if parent.right:
                stack.append((depth + 1, parent.right))
            if parent.left:
                stack.append((depth + 1, parent.left))

        values.reverse()

        return values


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.levelOrderBottom(root)
    print r
