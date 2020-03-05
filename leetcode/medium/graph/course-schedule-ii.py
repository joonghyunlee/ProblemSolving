class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        for curr, prev in prerequisites:
            graph[curr].append(prev)

        visit = [0] * numCourses
        def dfs(i, prefix):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True

            visit[i] = -1
            for j in graph[i]:
                if not dfs(j, prefix):
                    return False
            prefix.append(i)
            visit[i] = 1
            return True

        order = []
        for i in xrange(numCourses):
            if not dfs(i, order):
                return []
        return order


if __name__ == '__main__':
    s = Solution()
    prerequisites = [[1, 0]]
    r = s.findOrder(2, prerequisites)
    print r
    prerequisites = [[0, 1]]
    r = s.findOrder(2, prerequisites)
    print r
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    r = s.findOrder(4, prerequisites)
    print r
