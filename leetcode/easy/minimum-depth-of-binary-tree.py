# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = []
        queue.insert(0, (1, root))
        count = None
        while queue:
            depth, p = queue.pop()

            if not p.left and not p.right:
                count = min(depth, count) if count else depth
            if p.left:
                queue.insert(0, (depth + 1, p.left))
            if p.right:
                queue.insert(0, (depth + 1, p.right))

        return count

    def convert(self, nums):
        if not nums:
            return None

        root = TreeNode(nums[0])
        queue = []
        queue.insert(0, root)

        for i in range(1, len(nums), 2):
            p = queue.pop()
            if not p.left:
                if nums[i]:
                    p.left = TreeNode(nums[i])
                    queue.insert(0, p.left)
            if not p.right and i < len(nums) - 1:
                if nums[i + 1]:
                    p.right = TreeNode(nums[i + 1])
                    queue.insert(0, p.right)
        return root


if __name__ == '__main__':
    s = Solution()
    root = s.convert([3, 9, 20, None, None, 15, 7])
    r = s.minDepth(root)
    print r
