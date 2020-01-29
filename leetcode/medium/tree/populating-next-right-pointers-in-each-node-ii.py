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
        nodes = [cls(num) if num is not None else None
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
        prev = root
        while prev:
            curr = None
            leftmost = None
            while prev:
                leftmost = leftmost or prev.left or prev.right
                if prev.left and prev.right:
                    if curr:
                        curr.next = prev.left
                    prev.left.next = prev.right
                    curr = prev.right
                elif prev.left or prev.right:
                    if curr:
                        curr.next = (prev.left or prev.right)
                    curr = prev.left or prev.right
                prev = prev.next
            prev = leftmost
        return root


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, None, 7]
    root = Node.fromList(nums)
    s.connect(root)
    root.printNext()
    nums = [3, 9, 20, None, None, 15, 7]
    root = Node.fromList(nums)
    s.connect(root)
    root.printNext()
    nums = []
    root = Node.fromList(nums)
    s.connect(root)
    print(root)
