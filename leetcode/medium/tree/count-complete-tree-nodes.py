# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def fromList(cls, nums):
        nodes = [cls(num) if num else None for num in nums]
        n = len(nums)
        for i, node in enumerate(nodes):
            if node is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < n:
                node.left = nodes[li]
            if ri < n:
                node.right = nodes[ri]
        return nodes[0] if nodes else None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cnt = 0
        queue = [root]
        while queue:
            node = queue.pop()
            cnt += 1
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)
        return cnt


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, None]
    root = TreeNode.fromList(nums)
    r = s.countNodes(root)
    print r