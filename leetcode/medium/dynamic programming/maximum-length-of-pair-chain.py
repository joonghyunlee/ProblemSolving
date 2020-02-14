class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        pairs.sort(key=lambda x: x[0])
        memo = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            memo[i] = 1
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    memo[i] = max(memo[i], memo[j] + 1)
        return max(memo)

    def findLongestChain2(self, pairs):
        curr, total = float('-inf'), 0
        pairs.sort(key=lambda x: x[1])
        for x, y in pairs:
            if curr < x:
                curr = y
                total += 1
        return total


if __name__ == '__main__':
    s = Solution()
    pairs = [[1, 2], [4, 5], [3, 4]]
    r = s.findLongestChain(pairs)
    print r
    pairs = [[1, 2], [2, 3], [3, 4]]
    r = s.findLongestChain(pairs)
    print r
    pairs = [[-10, -8], [8, 9], [-5, 0], [6, 10],
             [-6, -4], [1, 7], [9, 10], [-4, 7]]
    r = s.findLongestChain(pairs)
    print r
