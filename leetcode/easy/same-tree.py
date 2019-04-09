# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val != q.val:
            return False

        if (not self.isSameTree(p.left, q.left) or
                not self.isSameTree(p.right, q.right)):
            return False

        return True

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        q1, q2 = [p], [q]
        while q1 and q2:
            n1, n2 = q1.pop(), q2.pop()
            if not n1 and not n2:
                continue
            elif not (n1 and n2):
                return False
            elif n1.val != n2.val:
                return False

            q1.insert(0, n1.left)
            q2.insert(0, n2.left)
            q1.insert(0, n1.right)
            q2.insert(0, n2.right)

        return True

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
    p = s.convertToTree([1, 2])
    q = s.convertToTree([1, None, 2])
    r = s.isSameTree(p, q)
    print(r)
    p = s.convertToTree([1, 2, 1])
    q = s.convertToTree([1, 1, 2])
    r = s.isSameTree(p, q)
    print(r)
    p = s.convertToTree([1, 2, 3])
    q = s.convertToTree([1, 2, 3])
    r = s.isSameTree(p, q)
    print(r)
