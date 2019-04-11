# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, ndic = [(0, root)], {}
        while q:
            d, p = q.pop()
            if not p:
                continue

            nodes = ndic.get(d, [])
            nodes.append(p.val)
            ndic[d] = nodes

            if p.left:
                q.insert(0, (d+1, p.left))
            if p.right:
                q.insert(0, (d+1, p.right))
        return list(ndic.values())

    def convertToTree(self, nums):
        nodes = [TreeNode(x) if x else None
                 for x in nums]
        for i, n in enumerate(nodes):
            if not n:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nodes):
                n.left = nodes[li]
            if ri < len(nodes):
                n.right = nodes[ri]
        return nodes[0]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    root = s.convertToTree(nums)
    r = s.levelOrder(root)
    print(r)
    r = s.levelOrder(None)
    print(r)
