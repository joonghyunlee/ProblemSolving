from graphviz import Digraph


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution:
    def inspectBalancedTree(self, root):
        def helper(node):
            if not node.left and not node.right:
                return True, 1

            l_balanced, l_height =\
                helper(node.left) if node.left else (True, 0)
            r_balanced, r_height =\
                helper(node.right) if node.right else (True, 0)

            balanced = abs(l_height - r_height) <= 1 \
                if l_balanced and r_balanced else False
            height = max(l_height, r_height) + 1

            return balanced, height

        balanced, _ = helper(root)
        return balanced

    def convertToTree(self, nums):
        nodes = list(map(lambda x: TreeNode(x) if x else None, nums))
        for i, n in enumerate(nodes):
            if not n:
                continue

            li = i * 2 + 1
            ri = i * 2 + 2
            n.left = nodes[li] if li < len(nodes) else None
            n.right = nodes[ri] if ri < len(nodes) else None

        return nodes[0]

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
    root = s.convertToTree(
        [1, 2, 3, None, None, None, 4, None,
         None, None, None, None, None, None, 5])
    s.printTree(root)
    r = s.inspectBalancedTree(root)
    print r
