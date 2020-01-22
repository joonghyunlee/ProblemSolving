# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return str(self.val)

    @classmethod
    def fromList(cls, nums):
        nodes = [cls(num) if nums is not None else None
                 for num in nums]
        n = len(nums)
        for i, node in enumerate(nodes):
            if not node:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < n:
                node.left = nodes[li]
            if ri < n:
                node.right = nodes[ri]
        return nodes[0] if nodes else None

    def printNext(self):
        q = [self]
        while q:
            node = q.pop()
            print node.next,
            if node.left:
                q.insert(0, node.left)
            if node.right:
                q.insert(0, node.right)
        print


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def pair(left, right):
            ln, rn = left, right
            while ln and rn:
                ln.next = rn
                ln = ln.right
                rn = rn.left

        def recursion(node):
            if not node:
                return
            pair(node.left, node.right)
            recursion(node.left)
            recursion(node.right)

        recursion(root)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    root = Node.fromList(nums)
    s.connect(root)
    root.printNext()
    nums = [1]
    root = Node.fromList(nums)
    s.connect(root)
    root.printNext()
    nums = []
    root = Node.fromList(nums)
    s.connect(root)
    print(root)
