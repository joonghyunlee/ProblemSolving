class Solution:
    def lastStoneWeight(self, stones: 'List[int]') -> int:
        import heapq
        q = [-stone for stone in stones]
        heapq.heapify(q)

        while len(q) > 1:
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            if first < second:
                heapq.heappush(q, first - second)
        return -q[0] if q else 0


if __name__ == '__main__':
    s = Solution()
    stones = [2, 7, 4, 1, 8, 1]
    r = s.lastStoneWeight(stones)
    print(r)
