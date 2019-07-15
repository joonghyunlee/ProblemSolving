# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, su):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        if not root:
            return paths

        q = [([root.val], root)]
        while q:
            path, n = q.pop()
            if not n.left and not n.right:
                if sum(path) == su:
                    paths.append(path)
                    continue
            if n.left:
                q.insert(0, (path + [n.left.val], n.left))
            if n.right:
                q.insert(0, (path + [n.right.val], n.right))
        return paths


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    r = s.pathSum(root, 22)
    print r
