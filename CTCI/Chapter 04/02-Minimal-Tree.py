from graphviz import Digraph


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution:
    def buildTree(self, nums):
        def helper(left, right):
            if left == right:
                return TreeNode(nums[left])

            mid = (left + right) // 2
            n = TreeNode(nums[mid])
            n.left = helper(left, mid-1)
            n.right = helper(mid+1, right)
            return n

        return helper(0, len(nums) - 1)

    def printTree(self, root):
        t = Digraph('binary_tree', directory='graph',
                    filename='binary_tree', format='png')
        t.attr(size='6,6')
        t.node_attr.update(color='lightblue2', style='filled', shape='circle')

        q = [root]
        while q:
            n = q.pop()
            if n.left:
                q.insert(0, n.left)
                t.edge(str(n.val), str(n.left.val))
            if n.right:
                q.insert(0, n.right)
                t.edge(str(n.val), str(n.right.val))
        t.view()


if __name__ == '__main__':
    s = Solution()
    r = s.buildTree([1, 2, 3, 4, 5, 6, 7])
    s.printTree(r)
