# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromList(cls, nums):
        n = len(nums)
        nodes = [cls(num) if num is not None else None for num in nums]
        for i, node in enumerate(nodes):
            if node is None:
                continue
            if i * 2 + 1 < n:
                node.left = nodes[i * 2 + 1]
            if i * 2 + 2 < n:
                node.right = nodes[i * 2 + 2]
        return nodes[0] if node else None


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def helper(node, target, depth):
            if not node:
                return -1, None
            elif node.left and node.left.val == target:
                return depth + 1, node
            elif node.right and node.right.val == target:
                return depth + 1, node

            dl, pl = helper(node.left, target, depth + 1)
            if dl > 0:
                return dl, pl
            dr, pr = helper(node.right, target, depth + 1)
            if dr > 0:
                return dr, pr

            return -1, None

        dx, px = helper(root, x, 0)
        dy, py = helper(root, y, 0)

        return (dx > 0 and dy > 0) and dx == dy and px != py


if __name__ == '__main__':
    s = Solution()
    root = TreeNode.fromList([1, 2, 3, 4])
    r = s.isCousins(root, 4, 3)
    print(r)
    root = TreeNode.fromList([1, 2, 3, None, 4, None, 5])
    r = s.isCousins(root, 5, 4)
    print(r)
