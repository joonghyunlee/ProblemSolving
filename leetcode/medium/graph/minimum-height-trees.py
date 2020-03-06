class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def findHeight(i):
            height = 0
            q = [(1, i)]
            visit = [0] * n
            while q:
                hi, cu = q.pop()
                height = max(height, hi)
                visit[cu] = 1
                for ne in graph[cu]:
                    if not visit[ne]:
                        q.insert(0, (hi + 1, ne))
            return height

        heights = [0] * n
        for i in range(n):
            heights[i] = findHeight(i)

        return list(filter(lambda i: heights[i] == min(heights), range(n)))

    # The root of MHT is the middle point of the longest path in the tree.
    # Hence there are at most two MHT roots.
    def findMinHeightTrees2(self, n, edges):
        if n == 1:
            return [0]
        import collections
        neighbors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # First find the leaves
        preLevel, unvisited = [], set(range(n))
        for i in range(n):
            if degrees[i] == 1:
                preLevel.append(i)

        while len(unvisited) > 2:
            thisLevel = []
            for u in preLevel:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited:
                        degrees[v] -= 1
                        if degrees[v] == 1:
                            thisLevel += [v]
            preLevel = thisLevel

        return preLevel


if __name__ == '__main__':
    s = Solution()
    edges = [[1, 0], [1, 2], [1, 3]]
    r = s.findMinHeightTrees(4, edges)
    print r
    r = s.findMinHeightTrees2(4, edges)
    print r
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    r = s.findMinHeightTrees(6, edges)
    print r
    r = s.findMinHeightTrees2(6, edges)
    print r
