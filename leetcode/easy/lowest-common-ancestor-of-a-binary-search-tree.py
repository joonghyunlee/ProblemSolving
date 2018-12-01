# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lancestor, rancestor = None, None
        queue = []
        queue.insert(0, (root, []))
        while queue:
            n, ancestor = queue.pop()
            if n == p:
                lancestor = ancestor + [n]
            elif n == q:
                rancestor = ancestor + [n]

            if n.left:
                queue.insert(0, (n.left, ancestor + [n]))
            if n.right:
                queue.insert(0, (n.right, ancestor + [n]))

        common = [a for a in lancestor if a in rancestor]
        return common[-1] if common else None


    def convertToTree(self, nums):
        if not nums:
            return None

        nodes = []
        for n in nums:
            nodes.append(TreeNode(n))

        for i, node in enumerate(nodes):
            lnode = nodes[i * 2 + 1] if i * 2 + 1 < len(nodes) else None
            rnode = nodes[i * 2 + 2] if i * 2 + 2 < len(nodes) else None

            node.left = lnode
            node.right = rnode

        return nodes

    def convertToList(self, root):
        nums = []
        queue = []

        if not root:
            return nums

        queue.insert(0, root)
        while queue:
            p = queue.pop()
            if p:
                nums.append(p.val)
                queue.insert(0, p.left)
                queue.insert(0, p.right)
            else:
                nums.append(None)
        return nums

    def dfsTraversal(self, root):
        if not root:
            return

        stack = []
        stack.append(root)
        while stack:
            p = stack.pop()
            print p.val,
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        print

    def bfsTraversal(self, root):
        if not root:
            return

        queue = []
        queue.insert(0, root)
        while queue:
            p = queue.pop()
            print p.val,
            if p.left:
                queue.insert(0, p.left)
            if p.right:
                queue.insert(0, p.right)
        print



if __name__ == '__main__':
    s = Solution()
    r = s.convertToTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    c = s.lowestCommonAncestor(r[0], r[1], r[3])
    print c.val
