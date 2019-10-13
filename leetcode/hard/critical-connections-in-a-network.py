class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = {i: list() for i in range(n)}
        for conn in connections:
            src, dst = conn
            graph.get(src).append(dst)
            graph.get(dst).append(src)

        visited = [-1] * n
        connections = set(map(tuple, (map(sorted, connections))))

        def dfs(node, parent, depth):
            if visited[node] >= 0:
                return visited[node]

            visited[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                back_depth = dfs(neighbor, node, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth

        dfs(0, 0, 0)

        return list(connections)


if __name__ == '__main__':
    s = Solution()
    r = s.criticalConnections(6, [
        [0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]
    ])
    print r
