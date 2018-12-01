# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def recur(n):
            if not n:
                return []
            if not (n.left or n.right):
                return [[str(n.val)]]
            if n.left:
                ll = recur(n.left)
                for l in ll:
                    l.insert(0, str(n.val))
            else:
                ll = []
            if n.right:
                rl = recur(n.right)
                for l in rl:
                    l.insert(0, str(n.val))
            else:
                rl = []
            return ll + rl
        paths = list(map(lambda x : '->'.join(x), recur(root)))
        return paths

    def convertToTree(self, nums):
        ns = list(map(lambda x: TreeNode(x) if x else None, nums))
        for i, n in enumerate(ns):
            if not n: continue
            li = i * 2 + 1
            ri = i * 2 + 2
            n.left = ns[li] if li < len(ns) else None
            n.right = ns[ri] if ri < len(ns) else None
        return ns[0]


if __name__ == '__main__':
    s = Solution()
    r = s.convertToTree([1, 2, 3, None, 5])
    print(s.binaryTreePaths(r))
    print(s.binaryTreePaths(None))
