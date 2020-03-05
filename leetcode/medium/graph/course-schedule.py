class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        import collections
        preMap = collections.defaultdict(set)

        for curr, prev in prerequisites:
            preMap[curr].add(prev)
            preMap[curr].update(preMap[prev])

            for value in preMap.values():
                if curr in value:
                    value.update(preMap[curr])

            if curr in preMap[prev]:
                return False

        return True

    def canFinish2(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for curr, prev in prerequisites:
            graph[curr].append(prev)
        
        visit = [0] * numCourses
        def isAcyclic(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not isAcyclic(j):
                    return False
            visit[i] = 1
            return True

        for i in xrange(numCourses):
            if not isAcyclic(i):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    prerequisites = [[1, 0]]
    r = s.canFinish(2, prerequisites)
    print r
    r = s.canFinish2(2, prerequisites)
    print r
    prerequisites = [[1, 0], [0, 1]]
    r = s.canFinish(2, prerequisites)
    print r
    r = s.canFinish2(2, prerequisites)
    print r
    prerequisites = [[1, 0], [1, 2], [0, 1]]
    r = s.canFinish(3, prerequisites)
    print r
    r = s.canFinish2(3, prerequisites)
    print r
    prerequisites = [[1, 0], [0, 2], [2, 1]]
    r = s.canFinish(3, prerequisites)
    print r
    r = s.canFinish2(3, prerequisites)
    print r
