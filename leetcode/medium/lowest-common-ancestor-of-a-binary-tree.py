# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def fromList(cls, nums):
        nodes = [cls(num) if num else None for num in nums]
        for i, node in enumerate(nodes):
            if node is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nums):
                node.left = nodes[li]
            if ri < len(nums):
                node.right = nodes[ri]
        return nodes[0]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node, p, q):
            if not node:
                return False, False, None

            pf, qf = False, False
            if node == p:
                pf = True
            if node == q:
                qf = True

            lpf, lqf, n = helper(node.left, p, q)
            if lpf and lqf:
                return lpf, lqf, n
            rpf, rqf, n = helper(node.right, p, q)
            if rpf and rqf:
                return rpf, rqf, n

            pf = pf or lpf or rpf
            qf = qf or lqf or rqf
            return pf, qf, node if pf and qf else None

        if p == q:
            return p

        _, _, common = helper(root, p, q)
        return common

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node, p, q):
            if not node:
                return None
            elif node in (p, q):
                return node

            l = helper(node.left, p, q)
            r = helper(node.right, p, q)

            return node if l and r else l or r
        return helper(root, p, q)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode.fromList(nums)
    r = s.lowestCommonAncestor(root, root.left, root.right)
    print(r)
    r = s.lowestCommonAncestor2(root, root.left, root.right)
    print(r)
    r = s.lowestCommonAncestor(root, root.left, root.left.left)
    print(r)
    r = s.lowestCommonAncestor2(root, root.left, root.left.left)
    print(r)
            

            