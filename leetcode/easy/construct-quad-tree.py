# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf,
                 topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def helper(l, r, n):
            if n == 1:
                return Node(True if grid[l][r] == 1 else False, True,
                            None, None, None, None)

            nn = n // 2
            lt = helper(l, r, nn)
            rt = helper(l, r + nn, nn)
            lb = helper(l + nn, r, nn)
            rb = helper(l + nn, r + nn, nn)

            if ((lt.val is not None and rt.val is not None and
                 lb.val is not None and rb.val is not None) and
                    (lt.val == rt.val and rt.val == lb.val and
                     lb.val == rb.val)):
                return Node(lt.val, True, None, None, None, None)
            else:
                return Node(None, False, lt, rt, lb, rb)
        return helper(0, 0, len(grid))

    def printQuadrupleTree(self, root):
        q = [(0, root)]
        while q:
            d, p = q.pop()
            print 'Level {}: {}, {}'.format(d, p.isLeaf, p.val)
            if p.topLeft:
                q.insert(0, (d + 1, p.topLeft))
            if p.topRight:
                q.insert(0, (d + 1, p.topRight))
            if p.bottomLeft:
                q.insert(0, (d + 1, p.bottomLeft))
            if p.bottomRight:
                q.insert(0, (d + 1, p.bottomRight))


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]
    ]
    r = s.construct(grid)
    # s.printQuadrupleTree(r)

    grid = [
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0]
    ]
    r = s.construct(grid)
    s.printQuadrupleTree(r)
