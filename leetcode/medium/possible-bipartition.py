class Solution:
    def possibleBipartition(self, N: int, dislikes: 'List[List[int]]') -> bool:
        def helper(nid: int, color: int) -> bool:
            colors[nid] = color
            for opposite in disMap[nid]:
                if colors[opposite] == color:
                    return False
                if colors[opposite] == 0 and not helper(opposite, -color):
                    return False
            return True

        if N == 1 or not dislikes:
            return True

        import collections
        disMap = collections.defaultdict(list)
        for n1, n2 in dislikes:
            disMap[n1].append(n2)
            disMap[n2].append(n1)

        colors = [0] * (N + 1)
        for nid in range(1, N + 1):
            if colors[nid] == 0 and (not helper(nid, 1)):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    N = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    r = s.possibleBipartition(N, dislikes)
    print(r)
    N = 10
    dislikes = [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]
    r = s.possibleBipartition(N, dislikes)
    print(r)
