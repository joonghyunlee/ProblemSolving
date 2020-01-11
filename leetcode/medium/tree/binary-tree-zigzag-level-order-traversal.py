# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def enqueue(q, n, d):
            if n:
                q.insert(0, (d+1, n))

        def helper(q, n, d):
            if not n:
                return
            enqueue(q, n.left, d)
            enqueue(q, n.right, d)

        q, vdic = [(0, root)], {}
        while q:
            d, p = q.pop()
            if not p:
                continue

            v = vdic.get(d, [])
            if d % 2 == 0:
                v.append(p.val)
            else:
                v.insert(0, p.val)
            vdic[d] = v
            helper(q, p, d)
        return list(vdic.values())


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.zigzagLevelOrder(root)
    print(r)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    r = s.zigzagLevelOrder(root)
    print(r)
