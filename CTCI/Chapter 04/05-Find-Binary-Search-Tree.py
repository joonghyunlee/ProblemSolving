class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def from_list(cls, nums):
        nodes = []
        for n in nums:
            if n:
                nodes.append(cls(n))
            else:
                nodes.append(n)
        for i, node in enumerate(nodes):
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nodes):
                node.left = nodes[li]
            if ri < len(nodes):
                node.right = nodes[ri]
        return nodes[0]


def isBinarySearchTree(root):
    def helper(nums, node):
        if not node:
            return
        if node.left:
            helper(nums, node.left)
        nums.append(node.val)
        helper(nums, node.right)
    nums = []
    helper(nums, root)

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


if __name__ == '__main__':
    root = TreeNode.from_list([5, 3, 7, 2, 4, 6, 8, 1])
    r = isBinarySearchTree(root)
    print r
    root = TreeNode.from_list([1, 2, 3, 4, 5, 6, 7, 8])
    r = isBinarySearchTree(root)
    print r
