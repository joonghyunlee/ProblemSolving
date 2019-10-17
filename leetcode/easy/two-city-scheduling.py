class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = len(costs)
        n = m // 2

        A, B = [], []
        for cost in costs:
            a, b = cost
            if a > b:
                B.append(cost)
            else:
                A.append(cost)

        A.sort(key=lambda x: x[1] - x[0], reverse=True)
        B.sort(key=lambda x: x[0] - x[1], reverse=True)

        while len(A) > n:
            B.append(A.pop())
        while len(B) > n:
            A.append(B.pop())

        return sum(map(lambda x: x[0], A)) + sum(map(lambda x: x[1], B))


if __name__ == '__main__':
    s = Solution()
    costs = [[10, 20], [30, 200], [400, 50], [30, 20], [10, 100], [50, 20]]
    r = s.twoCitySchedCost(costs)
    print r
    costs = [[259, 770], [448, 54], [926, 667],
             [184, 139], [840, 118], [577, 469]]
    r = s.twoCitySchedCost(costs)
    print r
