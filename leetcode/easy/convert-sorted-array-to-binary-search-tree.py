# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def convert(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = convert(nums[0:mid])
            root.right = convert(nums[mid+1:len(nums)])
            return root

        return convert(nums)

    def bfsTraversal(self, root):
        if not root:
            return

        queue = []
        queue.insert(0, root)
        while queue:
            p = queue.pop()
            if p.left:
                queue.insert(0, p.left)
            if p.right:
                queue.insert(0, p.right)

            print p.val,
        print


if __name__ == '__main__':
    s = Solution()
    r = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    s.bfsTraversal(r)
