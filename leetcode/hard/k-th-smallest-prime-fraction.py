class Solution:
    def kthSmallestPrimeFraction(self, A: 'List[int]', K: int) -> 'List[int]':
        import heapq
        fractions = []
        for i in range(len(A)):
            for j in range(i, len(A)):
                if A[i] < A[j]:
                    heapq.heappush(fractions, (A[i]/A[j], [A[i], A[j]]))

        answer = []
        while K > 0:
            _, answer = heapq.heappop(fractions)
            K -= 1
        return answer

    def kthSmallestPrimeFraction2(self, A: 'List[int]', K: int) -> 'List[int]':
        small, large = 0.0, 1.0
        p, q = 0, 0
        while large - small > 0.0000001:
            mid = (large + small) / 2
            cnt = 0
            j = 0
            minDiff = 1.0
            for i in range(1, len(A)):
                while j < i and A[j]/A[i] <= mid:
                    if minDiff > mid - A[j] / A[i]:
                        minDiff = mid - A[j] / A[i]
                        p = A[j]
                        q = A[i]
                    j += 1
                cnt += j
            if cnt == K:
                break
            if cnt < K:
                small = mid
            else:
                large = mid
        return (p, q)

    def kthSmallestPrimeFraction3(self, A: 'List[int]', K: int) -> 'List[int]':
        n = len(A)
        queue = []
        import heapq

        for i in range(n):
            heapq.heappush(queue, (A[0] / A[i], (i, 0)))

        while K > 1:
            _, p = heapq.heappop(queue)
            if p[1] + 1 < n:
                heapq.heappush(queue,
                               (A[p[1] + 1] / A[p[0]], (p[0], p[1] + 1)))
            K -= 1

        return (A[queue[0][1][1]], A[queue[0][1][0]]) if queue else []


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 5]
    r = s.kthSmallestPrimeFraction2(A, 3)
    print(r)
    A = [1, 2, 3, 5]
    r = s.kthSmallestPrimeFraction3(A, 3)
    print(r)
    A = [1, 7]
    r = s.kthSmallestPrimeFraction2(A, 1)
    print(r)
    A = [1, 7]
    r = s.kthSmallestPrimeFraction3(A, 1)
    print(r)
