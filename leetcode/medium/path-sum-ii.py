# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        return nodes[0] if n > 0 else None


class Solution(object):
    def pathSum(self, root, su):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        if not root:
            return paths

        q = [([root.val], root)]
        while q:
            path, n = q.pop()
            if not n.left and not n.right:
                if sum(path) == su:
                    paths.append(path)
                    continue
            if n.left:
                q.insert(0, (path + [n.left.val], n.left))
            if n.right:
                q.insert(0, (path + [n.right.val], n.right))
        return paths

    def pathSum2(self, root: TreeNode, sum: int) -> 'List[List[int]]':
        def helper(node: TreeNode, sum: int):
            if not node:
                return []
            elif not (node.left or node.right) and node.val == sum:
                return [[node.val]]

            m = []
            l = helper(node.left, sum - node.val)
            for li in l:
                li.insert(0, node.val)
                m.append(li)
            r = helper(node.right, sum - node.val)
            for ri in r:
                ri.insert(0, node.val)
                m.append(ri)
            return m
        return helper(root, sum)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode.fromList(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
    r = s.pathSum(root, 22)
    print(r)
    r = s.pathSum2(root, 22)
    print(r)
