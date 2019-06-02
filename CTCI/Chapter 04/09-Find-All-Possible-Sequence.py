import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findPossibleSequence(root):
    def weave(first, second, prefix, sequences):
        if len(first) == 0 or len(second) == 0:
            ret = copy.deepcopy(prefix)
            ret.extend(first)
            ret.extend(second)
            sequences.append(ret)
            return

        ff = first.pop(0)
        prefix.append(ff)
        weave(first, second, prefix, sequences)
        prefix.pop()
        first.insert(0, ff)

        sf = second.pop(0)
        prefix.append(sf)
        weave(first, second, prefix, sequences)
        prefix.pop()
        second.insert(0, sf)
        return

    def helper(node):
        if node is None:
            return [[]]
        ll = helper(node.left)
        rl = helper(node.right)

        ret = []
        for li in ll:
            for ri in rl:
                sequences = []
                weave(li, ri, [node.val], sequences)
                ret.extend(sequences)
        return ret

    return helper(root)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    r = findPossibleSequence(root)
    print r
