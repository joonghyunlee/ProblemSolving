# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def println(cls, root):
        queue = [root]
        while queue:
            node = queue.pop()
            print node,
            if node:
                queue.insert(0, node.left)
                queue.insert(0, node.right)
        print
        return


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def recursion(il, ir, pl, pr):
            if pl > pr:
                return None
            elif pl == pr:
                return TreeNode(postorder[pl])

            val = postorder[pr]
            ri = inorder.index(val)
            node = TreeNode(val)
            nl = recursion(il, ri - 1, pl, pl + (ri - il) - 1)
            nr = recursion(ri + 1, ir, pl + (ri - il), pr - 1)
            node.left = nl
            node.right = nr

            return node

        n = len(postorder)
        return recursion(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    s = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    r = s.buildTree(inorder, postorder)
    TreeNode.println(r)
    inorder = [9]
    postorder = [9]
    r = s.buildTree(inorder, postorder)
    TreeNode.println(r)
    inorder = []
    postorder = []
    r = s.buildTree(inorder, postorder)
    TreeNode.println(r)
