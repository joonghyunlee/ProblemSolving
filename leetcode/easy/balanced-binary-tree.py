# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare(r):
            if not r:
                return 0, True

            ldepth, ldiff = compare(r.left)
            rdepth, rdiff = compare(r.right)

            diff = ldepth - rdepth if ldepth > rdepth else rdepth - ldepth
            if diff == 1 or diff == 0:
                return max(ldepth, rdepth) + 1, (True and ldiff and rdiff)
            else:
                return max(ldepth, rdepth) + 1, False

        depth, diff = compare(root)
        return diff

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
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    r = s.isBalanced(root)
    print r
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    r = s.isBalanced(root)
    print r
    root = s.convert([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    r = s.isBalanced(root)
    print r
