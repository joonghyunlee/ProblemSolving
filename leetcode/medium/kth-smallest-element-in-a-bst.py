# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def from_list(cls, nums):
        nodes = [cls(n) if n else None for n in nums]
        for i, n in enumerate(nodes):
            if n is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            n.left = nodes[li] if li < len(nodes) else None
            n.right = nodes[ri] if ri < len(nodes) else None
        return nodes[0]


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nums = []
        st = []
        p = root
        while len(nums) < k:
            while p:
                st.append(p)
                p = p.left

            p = st.pop()
            nums.append(p.val)
            p = p.right

        return nums[-1]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode.from_list([3, 1, 4, None, 2])
    r = s.kthSmallest(root, 1)
    print r
    root = TreeNode.from_list([5, 3, 6, 2, 4, None, None, 1])
    r = s.kthSmallest(root, 3)
    print r
