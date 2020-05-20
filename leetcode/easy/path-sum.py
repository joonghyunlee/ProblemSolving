# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = []
        stack.append((root, root.val))

        while stack:
            p, s = stack.pop()

            if not p.left and not p.right:
                if s == sum:
                    return True

            if p.right:
                stack.append((p.right, p.right.val + s))
            if p.left:
                stack.append((p.left, p.left.val + s))

        return False

    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        def helper(node, sum):
            if not node:
                return False
            elif not node.left and not node.right:
                return node.val == sum

            return helper(node.left, sum - node.val) \
                or helper(node.right, sum - node.val)
        return helper(root, sum)

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
    root = s.convert([5, 4, 8, 11, None, 13, 4, 7, 2, None, 1])
    r = s.hasPathSum(root, 22)
    print(r)
    r = s.hasPathSum2(root, 22)
    print(r)
    root = s.convert([1])
    r = s.hasPathSum(root, 1)
    print(r)
    r = s.hasPathSum2(root, 1)
    print(r)
