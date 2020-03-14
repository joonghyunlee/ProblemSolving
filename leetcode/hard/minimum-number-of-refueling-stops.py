class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # (step, pos, fuel)
        q = [(0, 0, startFuel)]
        ans = []
        while q:
            step, pos, fuel = q.pop()
            if pos + fuel >= target:
                ans.append(step)
                continue

            for sPos, sFuel in stations:
                if sPos > pos and fuel >= (sPos - pos):
                    q.insert(0, (step + 1, sPos, fuel - (sPos - pos) + sFuel))

        return min(ans) if ans else -1

    def minRefuelStops2(self, target, startFuel, stations):
        memo = [startFuel] + [0] * len(stations)
        for i, (location, fuel) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if memo[t] >= location:
                    memo[t + 1] = max(memo[t + 1], memo[t] + fuel)
        for i, d in enumerate(memo):
            if d >= target:
                return i
        return -1

    def minRefuelStops3(self, target, startFuel, stations):
        import heapq
        pq = []
        cur = startFuel
        res = i = 0
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq: return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    stations = []
    r = s.minRefuelStops(1, 1, stations)
    print r
    r = s.minRefuelStops2(1, 1, stations)
    print r
    r = s.minRefuelStops3(1, 1, stations)
    print r

    stations = [[10, 100]]
    r = s.minRefuelStops(100, 1, stations)
    print r
    r = s.minRefuelStops2(100, 1, stations)
    print r
    r = s.minRefuelStops3(100, 1, stations)
    print r

    stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    r = s.minRefuelStops(100, 10, stations)
    print r
    r = s.minRefuelStops2(100, 10, stations)
    print r
    r = s.minRefuelStops3(100, 10, stations)
    print r

    stations = [[25, 30]]
    r = s.minRefuelStops(100, 50, stations)
    print r
    r = s.minRefuelStops2(100, 50, stations)
    print r
    r = s.minRefuelStops3(100, 50, stations)
    print r