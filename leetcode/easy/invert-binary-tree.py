# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        queue = []
        queue.insert(0, root)
        while queue:
            p = queue.pop()
            p.left, p.right = p.right, p.left

            if p.left: queue.insert(0, p.left)
            if p.right: queue.insert(0, p.right)

        return root

    def convertToTree(self, nums):
        if not nums:
            return None
        queue = []
        root = TreeNode(nums[0])
        queue.insert(0, (0, root))

        while queue:
            i, p = queue.pop()
            li = i * 2 + 1
            if li < len(nums):
                lp = TreeNode(nums[li])
                queue.insert(0, (li, lp))
            else:
                lp = None
            p.left = lp

            ri = i * 2 + 2
            if ri < len(nums):
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
            if p:
                nums.append(p.val)
                queue.insert(0, p.left)
                queue.insert(0, p.right)
            else:
                nums.append(None)
        return nums

    def dfsTraversal(self, root):
        if not root:
            return

        stack = []
        stack.append(root)
        while stack:
            p = stack.pop()
            print p.val,
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        print


if __name__ == '__main__':
    s = Solution()
    root = s.convertToTree([1,2,3,4,5,6,7])
    s.dfsTraversal(root)
    print(s.convertToList(root))
    s.invertTree(root)
    print(s.convertToList(root))

    root = s.convertToTree([4,2,7,1,3,6,9])
    s.invertTree(root)
    print(s.convertToList(root))

    root = s.convertToTree([1,2])
    print(s.convertToList(root))
    s.invertTree(root)
    print(s.convertToList(root))

    root = s.convertToTree([1])
    s.invertTree(root)
    print(s.convertToList(root))

    root = s.convertToTree([2,3,None,1])
    s.invertTree(root)
    print(s.convertToList(root))
