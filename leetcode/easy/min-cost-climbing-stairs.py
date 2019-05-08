class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        m = [0] * len(cost)
        m[0], m[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            m[i] = min(m[i-1] + cost[i],
                       m[i-2] + cost[i])
        return min(m[-1], m[-2])


if __name__ == '__main__':
    s = Solution()
    cost = [10, 15, 20]
    r = s.minCostClimbingStairs(cost)
    print(r)
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    r = s.minCostClimbingStairs(cost)
    print(r)
