# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isLeafNode(n):
            return not (n.left or n.right)

        if not root:
            return 0

        sum = 0
        queue = []
        queue.insert(0, root)

        while queue:
            p = queue.pop()
            lp, rp = p.left, p.right
            if lp:
                if isLeafNode(lp):
                    sum += lp.val
                else:
                    queue.insert(0, lp)
            if rp:
                queue.insert(0, rp)

        return sum

    def convertToTree(self, nums):
        if not nums:
            return None
        queue = []
        root = TreeNode(nums[0])
        queue.insert(0, (0, root))

        while queue:
            i, p = queue.pop()
            li = i * 2 + 1
            if li < len(nums) and nums[li]:
                lp = TreeNode(nums[li])
                queue.insert(0, (li, lp))
            else:
                lp = None
            p.left = lp

            ri = i * 2 + 2
            if ri < len(nums) and nums[ri]:
                rp = TreeNode(nums[ri])
                queue.insert(0, (ri, rp))
            else:
                rp = None
            p.right = rp

        return root

    def convertToList(self, root):
        nums = []
        queue = []

        if not root:
            return nums

        queue.insert(0, root)
        while queue:
            p = queue.pop()
            nums.append(p.val)

            if p.left:
                queue.insert(0, p.left)
            if p.right:
                queue.insert(0, p.right)
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    root = s.convertToTree(nums)
    r = s.sumOfLeftLeaves(root)
    print(r)
