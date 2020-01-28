# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rside = []
        if not root:
            return rside

        import collections
        nodeMap = collections.defaultdict(list)
        queue = [(0, root)]
        while queue:
            depth, node = queue.pop()
            nodeMap[depth].append(node)
            if node.left:
                queue.insert(0, (depth + 1, node.left))
            if node.right:
                queue.insert(0, (depth + 1, node.right))
            
        for nodes in nodeMap.values():
            rside.append(nodes[-1].val)

        return rside


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, None, 5, None, 4]
    root = TreeNode.fromList(nums)
    r = s.rightSideView(root)
    print r
    nums = []
    root = TreeNode.fromList(nums)
    r = s.rightSideView(root)
    print r