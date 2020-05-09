def solution(jobs):
    import heapq
    heapq.heapify(jobs)
    runq = []

    elapsed = 0
    waited = 0
    n = len(jobs)

    while jobs or runq:
        while jobs and elapsed >= jobs[0][0]:
            issued, required = heapq.heappop(jobs)
            heapq.heappush(runq, (required, issued))

        if runq:
            required, issued = heapq.heappop(runq)
            waited += (elapsed - issued if elapsed > issued else 0) \
                + required
            elapsed += required
        else:
            if jobs and elapsed < jobs[0][0]:
                elapsed = jobs[0][0]

    return waited // n if n > 0 else 0


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    r = solution(jobs)
    print(r)
    jobs = [[0, 3], [1, 9], [2, 6], [30, 3]]
    r = solution(jobs)
    print(r)