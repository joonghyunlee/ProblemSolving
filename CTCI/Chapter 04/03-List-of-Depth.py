class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

    def __repr__(self):
        return str(self.val)


class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x

    def __repr__(self):
        return self.val.__repr__()


class Solution:
    def getListOfDepth(self, root):
        if not root:
            return []

        ndic = {}
        q = [(0, root)]
        while q:
            depth, p = q.pop()
            new = ListNode(p)
            new.next = ndic.get(depth, None)
            ndic[depth] = new

            if p.left:
                q.insert(0, (depth+1, p.left))
            if p.right:
                q.insert(0, (depth+1, p.right))

        return ndic.values()

    def convertToTree(self, nums):
        nodes = [TreeNode(n) if n else None for n in nums]
        for i, n in enumerate(nodes):
            if n:
                li, ri = 2 * i + 1, 2 * i + 2
                n.left = nodes[li] if li < len(nums) else None
                n.right = nodes[ri] if ri < len(nums) else None
        return nodes[0]


if __name__ == '__main__':
    s = Solution()
    root = s.convertToTree(
        [1,
         2, 3,
         None, 4, 5, None,
         None, None, None, 6, 7, 8, None, None])
    r = s.getListOfDepth(root)
    for i, l in enumerate(r):
        print 'depth: %d: ' % i,
        p = l
        while p:
            print p,
            p = p.next
        print
