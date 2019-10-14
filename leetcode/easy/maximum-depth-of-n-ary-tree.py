# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        q = [(1, root)]
        max_depth = 0
        while q:
            depth, node = q.pop()
            max_depth = max(depth, max_depth)
            if not node.children:
                continue

            for child in node.children:
                q.insert(0, (depth + 1, child))

        return max_depth


if __name__ == '__main__':
    root = Node(1, None)
    root.children = [
        Node(2, None), Node(3, None), Node(4, None)
    ]
    root.children[0].children = [
        Node(5, None), Node(6, None)
    ]
    s = Solution()
    print(s.maxDepth(root))
