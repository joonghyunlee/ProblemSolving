# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def __str__(self, indent=""):
        rt = self.right.__str__(indent + "  ") if self.right else ""
        lt = self.left.__str__(indent + "  ") if self.left else ""

        return lt + "{}{}\n".format(indent, str(self.val)) + rt

    def __eq__(self, other) -> bool:
        if not isinstance(other, TreeNode):
            return False
        if self.val != other.val:
            return False
        
        return (self.left, self.right) == (other.left, other.right)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @classmethod
    def fromList(cls, nums):
        nodes = [cls(num) if num else None for num in nums]
        for i, node in enumerate(nodes):
            if node is None:
                continue
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(nums):
                node.left = nodes[li]
            if ri < len(nums):
                node.right = nodes[ri]
        return nodes[0] if nodes else None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        nums = []
        queue = [root]
        while queue:
            node = queue.pop()
            nums.append(str(node.val))

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

        return ','.join(nums)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(root, node):
            p = root
            while p:
                if p.val > node.val:
                    if not p.left:
                        return p
                    p = p.left
                else:
                    if not p.right:
                        return p
                    p = p.right
            return p

        if not data:
            return None

        nums = list(map(lambda x: int(x), data.split(',')))
        root = TreeNode(nums[0])
        for num in nums[1:]:
            node = TreeNode(num)
            parent = helper(root, node)
            if parent.val > node.val:
                parent.left = node
            else:
                parent.right = node

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    codec = Codec()
    root = TreeNode.fromList([2, 1, 3])
    copied = codec.deserialize(codec.serialize(root))
    print(root == copied)
    root = TreeNode.fromList([5, 3, 6, 2, 4, None, None, 1])
    copied = codec.deserialize(codec.serialize(root))
    print(root == copied)
