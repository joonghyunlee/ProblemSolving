# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(cls, nums):
        nodes = [cls(n) if n is not None else None for n in nums]
        for i, n in enumerate(nodes):
            if not n:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nodes):
                n.left = nodes[li]
            if ri < len(nodes):
                n.right = nodes[ri]
        return nodes[0]


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def findDescendants(root, distance, nodes):
            if not root:
                return
            q = [(0, root)]
            while q:
                depth, node = q.pop()
                if depth == distance:
                    nodes.append(node.val)
                if node.left:
                    q.insert(0, (depth + 1, node.left))
                if node.right:
                    q.insert(0, (depth + 1, node.right))
            return

        def search(root, target, nodes):
            if not root:
                return None
            if root == target:
                findDescendants(root, K, nodes)
                return 1

            lf = search(root.left, target, nodes)
            rf = search(root.right, target, nodes)

            if lf > 0 and rf is None:
                findDescendants(root.right, K - lf - 1, nodes)
            elif lf is None and rf > 0:
                findDescendants(root.left, K - rf - 1, nodes)

            distance = lf or rf
            if distance == K:
                nodes.append(root.val)

            return distance + 1 if distance is not None else None

        nodes = []
        search(root, target, nodes)

        return nodes


if __name__ == '__main__':
    s = Solution()
    nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = TreeNode.from_list(nums)
    target = root.left
    r = s.distanceK(root, target, 2)
    print r

    nums = [0, 1, None, 3, 2]
    root = TreeNode.from_list(nums)
    target = root.left.right
    r = s.distanceK(root, target, 1)
    print r

    nums = [0, 1, 3, 2, None, None, None, 4]
    root = TreeNode.from_list(nums)
    target = root.left
    r = s.distanceK(root, target, 0)
    print r