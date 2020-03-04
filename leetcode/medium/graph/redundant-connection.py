class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        sets = []
        ans = [0, 0]
        for u, v in edges:
            ui = None
            for i, se in enumerate(sets):
                if u in se:
                    ui = i
                    break
            vi = None
            for i, se in enumerate(sets):
                if v in se:
                    vi = i
                    break

            if ui is None and vi is None:
                sets.append({u, v})
            elif ui is not None and vi is None:
                sets[ui].add(v)
            elif ui is None and vi is not None:
                sets[vi].add(u)
            else:
                if ui == vi:
                    ans = [u, v]
                else:
                    sets[ui] = sets[ui].union(sets[vi])
                    del sets[vi]
        return ans

    def findRedundantConnection2(self, edges):
        parent = {}
        def find(node):
            return find(parent[node]) if node in parent else node

        for i, edge in enumerate(edges):
            root1, root2 = map(find, edge)
            if root1 == root2:
                return edge
            else:
                parent[root1] = parent[root2] = str(i)


if __name__ == '__main__':
    s = Solution()
    edges = [[1,2], [1,3], [2,3]]
    r = s.findRedundantConnection(edges)
    print r
    r = s.findRedundantConnection2(edges)
    print r
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    r = s.findRedundantConnection(edges)
    print r
    r = s.findRedundantConnection2(edges)
    print r