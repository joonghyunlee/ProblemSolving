# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s, p, prev = [], root, None
        while True:
            if p:
                s.append(p)
                p = p.left
            else:
                if not s:
                    break
                p = s.pop()

                if prev is None or prev < p.val:
                    prev = p.val
                else:
                    return False

                p = p.right

        return True

    def convertToTree(self, nums):
        nodes = [TreeNode(x) if x else None
                 for x in nums]
        for i, n in enumerate(nodes):
            if n is None:
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
    root = s.convertToTree([5, 1, 4, None, None, 3, 6])
    r = s.isValidBST(root)
    print r
    root = s.convertToTree([1, 2, 3, None, 4, None, 5])
    r = s.isValidBST(root)
    print r
    root = s.convertToTree([2, 1, 3])
    r = s.isValidBST(root)
    print r
    root = s.convertToTree([1, 1])
    r = s.isValidBST(root)
    print r
