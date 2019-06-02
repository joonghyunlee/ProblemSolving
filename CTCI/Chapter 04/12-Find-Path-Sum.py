class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    @classmethod
    def from_list(self, nums):
        nodes = []
        for n in nums:
            if n is not None:
                nodes.append(TreeNode(n))
            else:
                nodes.append(None)

        for i, node in enumerate(nodes):
            li = 2 * i + 1
            ri = 2 * i + 2
            if node:
                if li < len(nodes):
                    node.left = nodes[li]
                if ri < len(nodes):
                    node.right = nodes[ri]

        return nodes[0]


def findPathSum(root, x):
    def helper(node, seqs, x):
        next_seqs = [node.val]
        count = 0 if node.val != x else 1
        for s in seqs:
            next_seqs.append(s + node.val)
            if s + node.val == x:
                count += 1
        if node.left:
            count += helper(node.left, next_seqs, x)
        if node.right:
            count += helper(node.right, next_seqs, x)
        return count

    return helper(root, [], x)


def findPathSum2(root, x):
    def incMap(pMap, key, delta):
        new_val = pMap.get(key, 0) + delta
        if new_val == 0:
            del pMap[key]
        else:
            pMap[key] = new_val

    def helper(node, x, rs, pMap):
        if node is None:
            return 0

        rs += node.val
        count = pMap.get(rs - x, 0)
        if rs == x:
            count += 1

        incMap(pMap, rs, 1)
        count += helper(node.left, x, rs, pMap)
        count += helper(node.right, x, rs, pMap)
        incMap(pMap, rs, -1)

        return count

    return helper(root, x, 0, {})


if __name__ == '__main__':
    root = TreeNode.from_list([10, 5, -3, 3, 1, None, 11, 3, -2, None, 2])
    r = findPathSum(root, 8)
    print r
    r = findPathSum2(root, 8)
    print r
