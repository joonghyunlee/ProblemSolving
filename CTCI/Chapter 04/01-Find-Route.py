class Node:
    def __init__(self, x=None):
        self.val = x
        self.adjacents = []
        self.visited = False

    def __repr__(self):
        return str(self.val)


class Solution:
    def findRoute(self, start, end):
        q = [start]
        while q:
            n = q.pop()
            if n == end:
                return True

            n.visited = True
            for adjacent in n.adjacents:
                if not adjacent.visited:
                    q.insert(0, adjacent)

        return True if end.visited else False

    def convertToGraph(self, array):
        nodes = [Node(i) for i in range(len(array))]
        for source, edges in enumerate(array):
            for target, edge in enumerate(edges):
                if edge:
                    nodes[source].adjacents.append(nodes[target])
        return nodes


if __name__ == '__main__':
    s = Solution()
    array = [
        [False, True, True, False],
        [False, False, True, True],
        [False, False, False, False],
        [False, False, False, False]
    ]
    graph = s.convertToGraph(array)
    r = s.findRoute(graph[2], graph[3])
    print r
