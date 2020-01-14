# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def toList(cls, root):
        nodes = []
        if not root:
            return nodes

        q = [root]
        while q:
            node = q.pop()
            nodes.append(node)
            if node:
                q.insert(0, node.left)
                q.insert(0, node.right)
        
        return nodes


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def recursion(pl, pr, il, ir):
            if pl > pr:
                return None
            elif pl == pr:
                return TreeNode(preorder[pl])
            
            val = preorder[pl]
            idx = inorder.index(val)

            node = TreeNode(val)
            nl = recursion(pl + 1, pl + (idx - il), il, idx - 1)
            nr = recursion(pl + (idx - il) + 1, pr, idx + 1, ir)
            node.left = nl
            node.right = nr

            return node

        n = len(preorder)
        root = recursion(0, n - 1, 0, n - 1)

        return root


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    r = s.buildTree(preorder, inorder)
    nodes = TreeNode.toList(r)
    print nodes
    preorder = [1, 2, 3]
    inorder = [3, 2, 1]
    r = s.buildTree(preorder, inorder)
    nodes = TreeNode.toList(r)
    print nodes