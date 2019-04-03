# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(l, r):
            if l > r:
                return [None]
            elif l == r:
                return [TreeNode(l)]

            ret = []
            for m in range(l, r+1):
                lnodes = helper(l, m-1)
                rnodes = helper(m+1, r)

                for ln in lnodes:
                    for rn in rnodes:
                        root = TreeNode(m)
                        root.left = ln
                        root.right = rn
                        ret.append(root)
            return ret

        return helper(1, n)

    def printTree(self, root):
        q = [root]
        while q:
            n = q.pop()
            print n,
            if n:
                q.insert(0, n.left)
                q.insert(0, n.right)

if __name__ == '__main__':
    s = Solution()
    r = s.generateTrees(3)
    for n in r:
        print s.printTree(n)
